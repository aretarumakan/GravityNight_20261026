import json
import subprocess
import time

PRES_ID = "1xXP3MwI8Ew9fYXIqLqe5qA9cWuSpFSkdQMxDa7q8Zgs"

# 7 slides mapping
slides = [
    {"index": 0, "id": "p"},
    {"index": 1, "id": "SLIDES_API1080183801_0"},
    {"index": 2, "id": "SLIDES_API613279846_0"},
    {"index": 3, "id": "SLIDES_API1240383252_0"},
    {"index": 4, "id": "SLIDES_API559942963_0"},
    {"index": 5, "id": "SLIDES_API1961550828_0"},
    {"index": 6, "id": "SLIDES_API326219996_0"},
]

def get_elements_to_delete(slide_idx):
    res = subprocess.run(f"gslides readonly list-elements {PRES_ID} {slide_idx}", shell=True, capture_output=True, text=True)
    lines = res.stdout.strip().split("\n")
    to_delete = []
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 2:
            elem_id = parts[0]
            elem_type = parts[1]
            if elem_type == "shape":
                to_delete.append(elem_id)
    return to_delete

def run_batch(ops, label):
    path = f"/tmp/batch_fix_{label}.json"
    with open(path, "w") as f:
        json.dump(ops, f, ensure_ascii=False)
    res = subprocess.run(f"gslides mutate batch {PRES_ID} -f {path}", shell=True, capture_output=True, text=True)
    print(f"[{label}] Batch result: {res.stdout.strip() or res.stderr.strip()}")

def main():
    print("=== Applying Auditor Refinements to All Slides ===")

    # Slide 1
    s1_del = get_elements_to_delete(0)
    print(f"Slide 1 shapes to delete: {len(s1_del)}")
    ops1 = [{"op": "delete-element", "element": eid} for eid in s1_del]
    ops1.extend([
        # Google 4-Color Strip
        {"op": "add-textbox", "slide": "p", "text": "", "x": 0, "y": 0, "width": 180, "height": 3, "background_color": "#4285F4"},
        {"op": "add-textbox", "slide": "p", "text": "", "x": 180, "y": 0, "width": 180, "height": 3, "background_color": "#EA4335"},
        {"op": "add-textbox", "slide": "p", "text": "", "x": 360, "y": 0, "width": 180, "height": 3, "background_color": "#FBBC04"},
        {"op": "add-textbox", "slide": "p", "text": "", "x": 540, "y": 0, "width": 180, "height": 3, "background_color": "#34A853"},

        # Tag
        {"op": "add-textbox", "slide": "p", "text": "◆  GOOGLE DEEPMIND // EXECUTIVE ARCHITECTURE BRIEFING", "x": 40, "y": 26, "width": 380, "height": 24, "font_size": 9.5, "bold": True, "color": "#38BDF8", "background_color": "#0B1528", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},

        # Hero Title
        {"op": "add-textbox", "slide": "p", "text": "次世代 AI ペアプログラミングの全貌\nAntigravity × Gemini API CLI", "x": 40, "y": 65, "width": 640, "height": 85, "font_size": 30, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "line_spacing": 120},

        # Subtitle
        {"op": "add-textbox", "slide": "p", "text": "自律型エージェントの設計思想、ゼロトラスト境界、そしてコマンドライン OS への進化", "x": 40, "y": 158, "width": 640, "height": 26, "font_size": 12.5, "color": "#94A3B8"},

        # 3 Cards (Perfect 3-Line Alignment)
        {"op": "add-textbox", "slide": "p", "text": "🔒 100% ZERO-TRUST\n安全な権限分離設計\nプライベート情報と開発環境を厳格保護", "x": 40, "y": 205, "width": 200, "height": 125, "font_size": 11, "bold": True, "color": "#93C5FD", "background_color": "#0E1A33", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},
        {"op": "add-textbox", "slide": "p", "text": "📱 24/7 UNTETHERED\nどこからでも遠隔操作\nスマホから自律タスクを監視・即時承認", "x": 260, "y": 205, "width": 200, "height": 125, "font_size": 11, "bold": True, "color": "#D8B4FE", "background_color": "#1F1235", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},
        {"op": "add-textbox", "slide": "p", "text": "⚡ 1-LINE EXECUTION\n爆速マルチモーダル\n画像・動画・音声をコマンド一撃生成", "x": 480, "y": 205, "width": 200, "height": 125, "font_size": 11, "bold": True, "color": "#6EE7B7", "background_color": "#0A251E", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},

        # Footer
        {"op": "add-textbox", "slide": "p", "text": "Presented by aretarumakan  |  GravityNight 2026.10.27  |  Confidential & Proprietary", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "center"}
    ])
    run_batch(ops1, "slide1")
    time.sleep(1)

    # Slide 2
    sid2 = "SLIDES_API1080183801_0"
    s2_del = get_elements_to_delete(1)
    ops2 = [{"op": "delete-element", "element": eid} for eid in s2_del]
    ops2.extend([
        {"op": "add-textbox", "slide": sid2, "text": "DUAL ENGINE", "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid2, "text": "「統括部長」と「専門ツール」の完璧な役割分担 🤝", "x": 160, "y": 21, "width": 520, "height": 30, "font_size": 17, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"},

        # Left Card (Fixed single-line task highlight)
        {"op": "add-textbox", "slide": sid2, "text": "👔 ANTIGRAVITY CORE (プロジェクト統括)", "x": 40, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid2, "text": "• 広い視野でプロジェクト全体を設計・オーケストレーション\n• 複数ファイルの一括編集、自律デバッグ、自動テストの反復\n• Git / GitHub へのコミット・プッシュを完全管理\n• ブラウザ操作（DevTools）による実画面の検証・操作\n\n🎯 最適なタスク: 「Webアプリ実装」「コードベースのリファクタ」", "x": 40, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},

        # Right Card
        {"op": "add-textbox", "slide": sid2, "text": "⚡ GEMINI API CLI (超速の専門ツール)", "x": 370, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#34D399", "background_color": "#0A251E", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid2, "text": "• 過去ログを引きずらず、1行コマンドで超低遅延・最安実行\n• 画像・動画・音声・テキストのフルマルチモーダル即時出力\n• 外部依存ゼロの完全静的バイナリ（Go言語製）\n• エージェント向け構造化出力（TOON / 内蔵 jq）に完全対応\n\n🎯 最適なタスク: 「画像・音声の素材生成」「単発の高速ログ解析」", "x": 370, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},

        {"op": "add-textbox", "slide": sid2, "text": "Antigravity Executive Keynote  |  Slide 02", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops2, "slide2")
    time.sleep(1)

    # Slide 3
    sid3 = "SLIDES_API613279846_0"
    s3_del = get_elements_to_delete(2)
    ops3 = [{"op": "delete-element", "element": eid} for eid in s3_del]
    ops3.extend([
        {"op": "add-textbox", "slide": sid3, "text": "ZERO TRUST", "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": "#F43F5E", "background_color": "#2A0E14", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid3, "text": "なぜ Antigravity は Google Workspace に直結しないのか？ 🛡️", "x": 160, "y": 21, "width": 520, "height": 30, "font_size": 16.5, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"},

        # Banner
        {"op": "add-textbox", "slide": sid3, "text": "💡 「繋がらない」のではなく、あえて「直結させない」という鉄壁の安全思想。\n強力な実行権限を持つエージェントだからこそ、開発資産と個人のプライベートデータを厳格に分離しています。", "x": 40, "y": 66, "width": 640, "height": 42, "font_size": 11, "bold": True, "color": "#FDA4AF", "background_color": "#1C0D12", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 130},

        # Left Card
        {"op": "add-textbox", "slide": sid3, "text": "⚠️ デフォルト直結がもたらす致命的リスク", "x": 40, "y": 120, "width": 310, "height": 32, "font_size": 11.5, "bold": True, "color": "#F43F5E", "background_color": "#2A0E14", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid3, "text": "• 誤コミットの危険性:\n  個人の Gmail や社内機密文書を、AI が誤って公開 GitHub へ push する大事故\n\n• 広すぎる権限範囲:\n  シェル実行や外部通信権限を持つツールに、全社ドライブへのフリーパスを与えるリスク", "x": 40, "y": 155, "width": 310, "height": 190, "font_size": 11, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},

        # Right Card (No word splits)
        {"op": "add-textbox", "slide": sid3, "text": "🛡️ MCP（オープン規格）による正解のアプローチ", "x": 370, "y": 120, "width": 310, "height": 32, "font_size": 11.5, "bold": True, "color": "#34D399", "background_color": "#0A251E", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid3, "text": "• 最小権限の原則 (Least Privilege):\n  開発者が明示許可したスコープのみ、必要な時だけプラグインとして安全接続\n\n• ベンダーロックインの排除:\n  Google だけでなく、業界標準 MCP により自由かつ柔軟なツール連携が可能", "x": 370, "y": 155, "width": 310, "height": 190, "font_size": 11, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},

        {"op": "add-textbox", "slide": sid3, "text": "Antigravity Executive Keynote  |  Slide 03", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops3, "slide3")
    time.sleep(1)

    # Slide 4
    sid4 = "SLIDES_API1240383252_0"
    s4_del = get_elements_to_delete(3)
    ops4 = [{"op": "delete-element", "element": eid} for eid in s4_del]
    ops4.extend([
        {"op": "add-textbox", "slide": sid4, "text": "UNTETHERED", "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": "#A855F7", "background_color": "#1F1235", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "机からの完全な解放！Remote Control の技術的革新 📱", "x": 160, "y": 21, "width": 520, "height": 30, "font_size": 16.5, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"},

        # Card 1
        {"op": "add-textbox", "slide": sid4, "text": "📶 ANY NETWORK CONNECT\n同じ Wi-Fi にいなくても OK", "x": 40, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#D8B4FE", "background_color": "#1F1235", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "Google セキュア中継（リレー）を経由し、外出先のモバイル通信やカフェ Wi-Fi から手元の Mac へ安全直結。\n\n重いビルドやテストは Mac に任せ、手ぶらで身軽に移動できます。", "x": 40, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 145},

        # Card 2
        {"op": "add-textbox", "slide": sid4, "text": "📱 PURPOSE-BUILT UI\nスマホ専用のカード型画面", "x": 260, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "PC 画面の単なるミラーではなく、チャット・思考ログ・ファイル変更・承認ダイアログをスマホ専用に最適化。\n\n「ホーム画面に追加」でネイティブアプリ同様にワンタップ起動！", "x": 260, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 145},

        # Card 3
        {"op": "add-textbox", "slide": sid4, "text": "🚨 ONE-CLICK REVOKE\n登壇・配信時も安心の防衛", "x": 480, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#F43F5E", "background_color": "#2A0E14", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "配信等でうっかり QR コードを見られても、「Enable Remote Control」を OFF ➔ ON でトークン即時破棄。\n\n古いリンクからのアクセスを即座に 100% 無力化できます。", "x": 480, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 145},

        {"op": "add-textbox", "slide": sid4, "text": "Antigravity Executive Keynote  |  Slide 04", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops4, "slide4")
    time.sleep(1)

    # Slide 5
    sid5 = "SLIDES_API559942963_0"
    s5_del = get_elements_to_delete(4)
    ops5 = [{"op": "delete-element", "element": eid} for eid in s5_del]
    ops5.extend([
        {"op": "add-textbox", "slide": sid5, "text": "COMMAND LINE OS", "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": "#34D399", "background_color": "#0A251E", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
        # Width increased to 540 so ⚡ never breaks
        {"op": "add-textbox", "slide": sid5, "text": "破壊的スピード！Gemini API CLI のフルマルチモーダル実機検証 ⚡", "x": 160, "y": 21, "width": 540, "height": 30, "font_size": 16, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"},

        # Left Column (Tuned 2-line endings)
        {"op": "add-textbox", "slide": sid5, "text": "🎨 画像生成 (gemini-api image)\n$ gemini-api image \"A cute robot...\" --out robot.jpg\nプロンプトから数秒で画像出力。アスペクト比 16:9 や 2K/4K に完全対応。", "x": 40, "y": 68, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
        {"op": "add-textbox", "slide": sid5, "text": "🎬 動画生成 720p (gemini-api video)\n$ gemini-api video \"Cinematic overview...\" --resolution 720p\n未来的な映像を MP4 出力。Shorts用縦型（9:16）や会話型編集に対応。", "x": 40, "y": 138, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
        {"op": "add-textbox", "slide": sid5, "text": "🔊 音声合成 (gemini-api tts)\n$ gemini-api tts \"Googleから発表された...\" --out narration.wav\nクリアな日本語音声を即時 WAV 生成。Mac の afplay で即座に再生。", "x": 40, "y": 208, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
        {"op": "add-textbox", "slide": sid5, "text": "🔍 解析 & 構造化出力 (gemini-api analyze)\n$ gemini-api analyze code.py --output-format json --jq .summary\nコード・PDF・YouTube 動画を直接指定。内蔵 jq でパイプライン連携も自在。", "x": 40, "y": 278, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},

        # Right Side Badge
        {"op": "add-textbox", "slide": sid5, "text": "◆ 実機生成画像: robot.jpg (gemini-api image / 2K)", "x": 420, "y": 68, "width": 260, "height": 24, "font_size": 10, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},

        {"op": "add-textbox", "slide": sid5, "text": "Antigravity Executive Keynote  |  Slide 05", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops5, "slide5")
    time.sleep(1)

    # Slide 6
    sid6 = "SLIDES_API1961550828_0"
    s6_del = get_elements_to_delete(5)
    ops6 = [{"op": "delete-element", "element": eid} for eid in s6_del]
    ops6.extend([
        {"op": "add-textbox", "slide": sid6, "text": "EXTENSIONS", "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid6, "text": "エージェントを拡張する！@メンションの極意 ＆ マーケットプレイス 🎁", "x": 160, "y": 21, "width": 540, "height": 30, "font_size": 16, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"},

        # Left Card
        {"op": "add-textbox", "slide": sid6, "text": "🏷️ 開発を加速する @メンションの奥義", "x": 40, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid6, "text": "• @conversation（スマートな文脈圧縮）:\n  会話が長くなったら新規スレッドを立てて @conversation。過去のゴミ生ログを削ぎ落とし、決定事項と成果物だけを美しく引き継いで思考ブレを完全リセット！\n\n• @rules（行動規約・校則の徹底）:\n  「日本語コメント必須」「TypeScript の any 禁止」など、AI に絶対守らせたいルールをいつでも一瞬で強制適用。\n\n• @file / @folder / @terminal:\n  見せたいコードやターミナルの出力をピンポイントで手渡し。", "x": 40, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 140},

        # Right Card (No word splits)
        {"op": "add-textbox", "slide": sid6, "text": "🛍️ Customizations Marketplace (公式ストア)", "x": 370, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#A855F7", "background_color": "#1F1235", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid6, "text": "• 「+」ボタン 1 つで即座にインストール:\n  Google Workspace（Docs, Sheets, Slides, Drive, Calendar）の公式拡張がワンタップで導入可能。\n\n• CLI とプラグインは競合しない！:\n  マーケットプレイスは「AI の知識」、CLI は手元の「万能ツール」。役割が違うため干渉せず、相乗効果でスマートに動作！\n\n• 公式 SDK ＆ ツール群:\n  Firebase や Chrome DevTools など Google 公式ツールを自在に増設可能。", "x": 370, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 140},

        {"op": "add-textbox", "slide": sid6, "text": "Antigravity Executive Keynote  |  Slide 06", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops6, "slide6")
    time.sleep(1)

    # Slide 7
    sid7 = "SLIDES_API326219996_0"
    s7_del = get_elements_to_delete(6)
    ops7 = [{"op": "delete-element", "element": eid} for eid in s7_del]
    ops7.extend([
        {"op": "add-textbox", "slide": sid7, "text": "SPECIAL APPENDIX", "x": 40, "y": 20, "width": 120, "height": 22, "font_size": 9.5, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
        # Expanded width to 530 so 📊 never breaks
        {"op": "add-textbox", "slide": sid7, "text": "Gemini API CLI (v0.4.4) 包括的アーキテクチャ・インフォグラフィック 📊", "x": 170, "y": 18, "width": 530, "height": 28, "font_size": 13.5, "bold": True, "color": "#F8FAFC", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid7, "text": "※ gemini-api image (2K) 実機生成によるアーキテクチャ概念図・ロードマップ概要  |  Antigravity Executive Keynote", "x": 40, "y": 378, "width": 640, "height": 18, "font_size": 9, "color": "#94A3B8", "alignment": "center"}
    ])
    run_batch(ops7, "slide7")

    print("\n=== All Refinements Successfully Applied! ===")

if __name__ == "__main__":
    main()
