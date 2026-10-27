import json
import subprocess
import time
import os

PRES_ID = "1xXP3MwI8Ew9fYXIqLqe5qA9cWuSpFSkdQMxDa7q8Zgs"
WORKSPACE = "/Users/SA_Tera/Desktop/anti20261026"
BG_COVER = f"{WORKSPACE}/keynote_bg_dark.jpg"
BG_CONTENT = f"{WORKSPACE}/slide_bg_clean.jpg"
IMG_ROBOT = f"{WORKSPACE}/robot.jpg"
IMG_INFO = f"{WORKSPACE}/infographic_ja.jpg"

def run_cmd(cmd):
    print(f"Running: {cmd[:100]}...")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR: {res.stderr}")
    return res

def get_slide_ids():
    res = subprocess.run(f"gslides readonly list-slides {PRES_ID} --json", shell=True, capture_output=True, text=True)
    try:
        data = json.loads(res.stdout)
        return [s["id"] for s in data]
    except Exception as e:
        # fallback parsing
        lines = res.stdout.strip().split("\n")
        ids = []
        for line in lines[2:]:
            parts = line.split()
            if len(parts) >= 2:
                ids.append(parts[1])
        return ids

def main():
    print(f"Building master presentation: {PRES_ID}")
    
    # Check current slides
    slides = get_slide_ids()
    print(f"Initial slides: {slides}")
    
    # Step 1: Populate Slide 1 (Cover)
    print("\n--- Constructing Slide 1: Cover ---")
    cover_batch = [
        # Top Google Spectrum Strip
        {"op": "add-textbox", "slide": "p", "text": "", "x": 0, "y": 0, "width": 180, "height": 3, "background_color": "#4285F4"},
        {"op": "add-textbox", "slide": "p", "text": "", "x": 180, "y": 0, "width": 180, "height": 3, "background_color": "#EA4335"},
        {"op": "add-textbox", "slide": "p", "text": "", "x": 360, "y": 0, "width": 180, "height": 3, "background_color": "#FBBC04"},
        {"op": "add-textbox", "slide": "p", "text": "", "x": 540, "y": 0, "width": 180, "height": 3, "background_color": "#34A853"},

        # 3 High-Impact Cards
        {"op": "add-textbox", "slide": "p", "text": "🔒 100% ZERO-TRUST\n安全な権限分離設計\nプライベート情報と開発環境を厳格に保護", "x": 40, "y": 225, "width": 200, "height": 115, "font_size": 11, "bold": True, "color": "#93C5FD", "background_color": "#0E1A33", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},
        {"op": "add-textbox", "slide": "p", "text": "📱 24/7 UNTETHERED\nどこからでも遠隔操作\nスマホから自律タスクの監視・即時承認", "x": 260, "y": 225, "width": 200, "height": 115, "font_size": 11, "bold": True, "color": "#D8B4FE", "background_color": "#1F1235", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},
        {"op": "add-textbox", "slide": "p", "text": "⚡ 1-LINE EXECUTION\n爆速マルチモーダル\n画像・動画・音声をコマンド一撃で生成", "x": 480, "y": 225, "width": 200, "height": 115, "font_size": 11, "bold": True, "color": "#6EE7B7", "background_color": "#0A251E", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},

        # Footer
        {"op": "add-textbox", "slide": "p", "text": "Presented by aretarumakan  |  GravityNight 2026.10.27  |  Confidential & Proprietary", "x": 40, "y": 370, "width": 640, "height": 18, "font_size": 9.5, "color": "#94A3B8", "alignment": "center"}
    ]
    with open("/tmp/batch_slide1.json", "w") as f:
        json.dump(cover_batch, f)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/batch_slide1.json")

    # Helper for adding content slide with background image
    slides_def = [
        {
            "id": "SLIDE_2",
            "tag": "DUAL ENGINE",
            "tag_color": "#38BDF8",
            "tag_bg": "#0E1A33",
            "title": "「統括部長」と「専門ツール」の完璧な役割分担 🤝",
            "boxes": [
                {"text": "👔 ANTIGRAVITY CORE (プロジェクト統括)", "x": 40, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "• 広い視野でプロジェクト全体を設計・オーケストレーション\n• 複数ファイルの一括編集、自律デバッグ、自動テストの反復\n• Git / GitHub へのコミット・プッシュを完全管理\n• ブラウザ操作（DevTools）による実画面の検証・操作\n\n🎯 最適なタスク: 「Webアプリ全体の実装」「コードベースのリファクタ」", "x": 40, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},
                {"text": "⚡ GEMINI API CLI (超速の専門ツール)", "x": 370, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#34D399", "background_color": "#0A251E", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "• 過去ログを引きずらず、1行コマンドで超低遅延・最安実行\n• 画像・動画・音声・テキストのフルマルチモーダル即時出力\n• 外部依存ゼロの完全静的バイナリ（Go言語製）\n• エージェント向け構造化出力（TOON / 内蔵 jq）に完全対応\n\n🎯 最適なタスク: 「画像・音声の素材生成」「単発の高速ログ解析」", "x": 370, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},
                {"text": "Antigravity Executive Keynote  |  Slide 02", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
            ]
        },
        {
            "id": "SLIDE_3",
            "tag": "ZERO TRUST",
            "tag_color": "#F43F5E",
            "tag_bg": "#2A0E14",
            "title": "なぜ Antigravity は Google Workspace に直結しないのか？ 🛡️",
            "boxes": [
                {"text": "💡 「繋がらない」のではなく、あえて「直結させない」という鉄壁の安全思想。\n強力な実行権限を持つエージェントだからこそ、開発資産と個人のプライベートデータを厳格に分離しています。", "x": 40, "y": 68, "width": 640, "height": 40, "font_size": 11, "bold": True, "color": "#FDA4AF", "background_color": "#1C0D12", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "⚠️ デフォルト直結がもたらす致命的リスク", "x": 40, "y": 120, "width": 310, "height": 32, "font_size": 11.5, "bold": True, "color": "#F43F5E", "background_color": "#2A0E14", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "• 誤コミットの危険性:\n  個人の Gmail や社内機密文書を、AI が誤って公開 GitHub に push してしまう大事故\n\n• 広すぎる権限範囲:\n  シェルコマンド実行や外部通信権限を持つツールに、全社ドライブへのフリーパスを与えるリスク", "x": 40, "y": 155, "width": 310, "height": 190, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "🛡️ MCP（オープン規格）による正解のアプローチ", "x": 370, "y": 120, "width": 310, "height": 32, "font_size": 11.5, "bold": True, "color": "#34D399", "background_color": "#0A251E", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "• 最小権限の原則 (Least Privilege):\n  開発者が明示的に許可したスコープだけを、必要な時だけプラグインとして安全に接続\n\n• ベンダーロックインの排除:\n  Google だけでなく、業界共通の標準プロトコル（MCP）により自由なツール連携が可能", "x": 370, "y": 155, "width": 310, "height": 190, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "Antigravity Executive Keynote  |  Slide 03", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
            ]
        },
        {
            "id": "SLIDE_4",
            "tag": "UNTETHERED",
            "tag_color": "#A855F7",
            "tag_bg": "#1F1235",
            "title": "机からの完全な解放！Remote Control の技術的革新 📱",
            "boxes": [
                {"text": "📶 ANY NETWORK CONNECT\n同じ Wi-Fi にいなくても OK", "x": 40, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#D8B4FE", "background_color": "#1F1235", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "Google のセキュアなクラウド中継（リレー）を経由するため、外出先のモバイル通信（4G/5G）やカフェの Wi-Fi からでも手元の Mac に安全直結。\n\n重いビルドやテストは Mac に任せ、手ぶらで移動できます。", "x": 40, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "📱 PURPOSE-BUILT UI\nスマホ専用のカード型画面", "x": 260, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "PC 画面の単なるミラーリングではなく、チャット・思考ログ・ファイル変更・承認ダイアログがスマホで見やすく設計。\n\n「ホーム画面に追加」するだけで、ネイティブアプリ同様にワンタップ起動！", "x": 260, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "🚨 ONE-CLICK REVOKE\n登壇・配信時も安心の防衛", "x": 480, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#F43F5E", "background_color": "#2A0E14", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "セミナーや配信でうっかり QR コードを見られても、「Enable Remote Control」を OFF ➔ ON にするだけでトークン即時破棄。\n\n古いリンクからは 100% アクセス不可になり即座に無力化できます。", "x": 480, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "Antigravity Executive Keynote  |  Slide 04", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
            ]
        },
        {
            "id": "SLIDE_5",
            "tag": "COMMAND LINE OS",
            "tag_color": "#34D399",
            "tag_bg": "#0A251E",
            "title": "破壊的スピード！Gemini API CLI のフルマルチモーダル実機検証 ⚡",
            "boxes": [
                {"text": "🎨 画像生成 (gemini-api image)\n$ gemini-api image \"A cute robot...\" --out robot.jpg\nプロンプトから数秒で画像出力。アスペクト比 16:9 や 2K/4K に完全対応。", "x": 40, "y": 68, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
                {"text": "🎬 動画生成 720p (gemini-api video)\n$ gemini-api video \"Cinematic overview...\" --resolution 720p\n未来的な映像を MP4 で書き出し。Shorts用縦動画（9:16）や会話型編集も可能。", "x": 40, "y": 138, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
                {"text": "🔊 音声合成 (gemini-api tts)\n$ gemini-api tts \"Googleから発表された...\" --out narration.wav\nテキストからクリアな日本語音声を即時 WAV 生成。Mac の afplay で即時再生。", "x": 40, "y": 208, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
                {"text": "🔍 解析 & 構造化出力 (gemini-api analyze)\n$ gemini-api analyze code.py --output-format json --jq .summary\nコード・PDF・YouTube 動画を直接指定。内蔵 jq でパイプライン連携も自在。", "x": 40, "y": 278, "width": 360, "height": 62, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 130},
                {"text": "◆ 実機生成画像: robot.jpg (gemini-api image / 2K)", "x": 420, "y": 68, "width": 260, "height": 24, "font_size": 10, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "Antigravity Executive Keynote  |  Slide 05", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
            ],
            "extra_image": {"file": IMG_ROBOT, "x": 420, "y": 98, "width": 260, "height": 242}
        },
        {
            "id": "SLIDE_6",
            "tag": "EXTENSIONS",
            "tag_color": "#38BDF8",
            "tag_bg": "#0E1A33",
            "title": "エージェントを拡張する！@メンションの極意 ＆ マーケットプレイス 🎁",
            "boxes": [
                {"text": "🏷️ 開発を加速する @メンションの奥義", "x": 40, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "• @conversation（スマートな文脈圧縮）:\n  会話が長くなったら新規スレッドを立てて @conversation。過去のゴミ生ログを削ぎ落とし、決定事項と成果物だけを美しく引き継いで思考ブレを完全リセット！\n\n• @rules（行動規約・校則の徹底）:\n  「日本語コメント必須」「TypeScript の any 禁止」など、AI に絶対守らせたいルールをいつでも一瞬で強制適用。\n\n• @file / @folder / @terminal:\n  見せたいコードやターミナルの出力をピンポイントで手渡し。", "x": 40, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "🛍️ Customizations Marketplace (公式ストア)", "x": 370, "y": 68, "width": 310, "height": 34, "font_size": 12, "bold": True, "color": "#A855F7", "background_color": "#1F1235", "alignment": "center", "content_alignment": "MIDDLE"},
                {"text": "• 「+」ボタン 1 つで即座にインストール:\n  Google Workspace（Docs, Sheets, Slides, Drive, Calendar）の公式拡張がワンタップで導入可能。\n\n• CLI とプラグインは競合しない！:\n  マーケットプレイスのプラグインは「AI の知識・教科書」、CLI は「机の上の道具」。レイヤーが違うためごっちゃにならず、むしろ相乗効果で賢く動作！\n\n• 公式 SDK ＆ ツール群:\n  Firebase や Chrome DevTools など Google 公式ツールを自在に増設可能。", "x": 370, "y": 105, "width": 310, "height": 240, "font_size": 10.5, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 140},
                {"text": "Antigravity Executive Keynote  |  Slide 06", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
            ]
        },
        {
            "id": "SLIDE_7",
            "tag": "SPECIAL APPENDIX",
            "tag_color": "#38BDF8",
            "tag_bg": "#0E1A33",
            "title": "Gemini API CLI (v0.4.4) 包括的アーキテクチャ・インフォグラフィック 📊",
            "is_cover_bg": True,
            "boxes": [
                {"text": "Antigravity Executive Keynote  |  Slide 07", "x": 40, "y": 380, "width": 640, "height": 18, "font_size": 9, "color": "#64748B", "alignment": "right"}
            ],
            "extra_image": {"file": IMG_INFO, "x": 100, "y": 55, "width": 520, "height": 315}
        }
    ]

    for s in slides_def:
        sid = s["id"]
        print(f"\n--- Adding slide {sid} ---")
        # 1. Add blank slide
        run_cmd(f"gslides mutate add-slide {PRES_ID} --layout BLANK")
        time.sleep(1)
        current_slides = get_slide_ids()
        new_slide_id = current_slides[-1]
        print(f"New slide created with ID: {new_slide_id}")

        # 2. Insert Background Image First (so it sits at the bottom layer)
        bg_file = BG_COVER if s.get("is_cover_bg") else BG_CONTENT
        run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{new_slide_id}" --file "{bg_file}" --x 0 --y 0 --width 720 --height 405')
        time.sleep(1)

        # 3. Add textboxes and cards
        batch = [
            {"op": "add-textbox", "slide": new_slide_id, "text": s["tag"], "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": s["tag_color"], "background_color": s["tag_bg"], "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
            {"op": "add-textbox", "slide": new_slide_id, "text": s["title"], "x": 160, "y": 21, "width": 520, "height": 30, "font_size": 17, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"}
        ]
        for b in s["boxes"]:
            item = {"op": "add-textbox", "slide": new_slide_id, "text": b["text"], "x": b["x"], "y": b["y"], "width": b["width"], "height": b["height"], "font_size": b.get("font_size", 11), "color": b.get("color", "#F8FAFC")}
            if "bold" in b: item["bold"] = b["bold"]
            if "background_color" in b: item["background_color"] = b["background_color"]
            if "font_family" in b: item["font_family"] = b["font_family"]
            if "alignment" in b: item["alignment"] = b["alignment"]
            if "content_alignment" in b: item["content_alignment"] = b["content_alignment"]
            if "line_spacing" in b: item["line_spacing"] = b["line_spacing"]
            batch.append(item)

        batch_path = f"/tmp/batch_{sid}.json"
        with open(batch_path, "w") as f:
            json.dump(batch, f, ensure_ascii=False)
        run_cmd(f"gslides mutate batch {PRES_ID} -f {batch_path}")
        time.sleep(1)

        # 4. Insert Extra Image if any
        if "extra_image" in s:
            img = s["extra_image"]
            run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{new_slide_id}" --file "{img["file"]}" --x {img["x"]} --y {img["y"]} --width {img["width"]} --height {img["height"]}')
            time.sleep(1)

    print("\nPresentation creation complete!")

if __name__ == "__main__":
    main()
