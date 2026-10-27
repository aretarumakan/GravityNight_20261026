import json
import subprocess
import time
import os
import glob

PRES_ID = "17rAr4235_WVL6Pqi-58sMdWhIqwrH33EFhFo2f_JuCE"
WORKSPACE = "/Users/SA_Tera/Desktop/anti20261026"
IMG_ROBOT = f"{WORKSPACE}/robot.jpg"
IMG_INFO = f"{WORKSPACE}/infographic_ja.jpg"

def run_cmd(cmd):
    print(f"Running: {cmd[:115]}...")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"ERROR: {res.stderr.strip()}")
    else:
        print(f"OK: {res.stdout.strip()}")
    return res

def add_blank_slide():
    res = subprocess.run(f"gslides mutate add-slide {PRES_ID}", shell=True, capture_output=True, text=True)
    slide_id = res.stdout.strip().replace("Added slide: ", "").strip()
    print(f"Added slide: {slide_id}")
    return slide_id

def tb(slide, text, x, y, w, h, size=10.5, color="#F8FAFC", bg=None, bold=False, align=None, valign=None, spacing=None, font="Montserrat"):
    if text == "":
        op = {
            "op": "add-textbox",
            "slide": slide,
            "text": "",
            "x": x,
            "y": y,
            "width": w,
            "height": h,
        }
        if bg: op["background_color"] = bg
        return op
    op = {
        "op": "add-textbox",
        "slide": slide,
        "text": text,
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "font_size": size,
        "color": color,
        "font_family": font
    }
    if bold: op["bold"] = True
    if bg: op["background_color"] = bg
    if align: op["alignment"] = align
    if valign: op["content_alignment"] = valign
    if spacing: op["line_spacing"] = spacing
    return op

def header_ops(slide, badge_text, title_text, accent="#F59E0B", badge_bg="#271A0C"):
    return [
        # Top subtle accent bar
        tb(slide, "", 40, 18, 4, 28, bg=accent),
        tb(slide, badge_text, 50, 21, 135, 22, size=9, color=accent, bg=badge_bg, bold=True, align="center", valign="MIDDLE"),
        tb(slide, title_text, 195, 18, 485, 28, size=16, color="#F8FAFC", bold=True, valign="MIDDLE"),
        # Footer
        tb(slide, "Antigravity × Gemini API CLI  |  Argon Architectural Edition", 40, 372, 450, 16, size=8.5, color="#64748B"),
    ]

def main():
    bg_cover = f"{WORKSPACE}/argon_bg_cover.jpg"
    bg_content = f"{WORKSPACE}/argon_bg_content.jpg"
    if not os.path.exists(bg_cover):
        bg_cover = f"{WORKSPACE}/keynote_bg_dark.jpg"
    if not os.path.exists(bg_content):
        bg_content = f"{WORKSPACE}/slide_bg_clean.jpg"

    print(f"Using cover BG: {bg_cover}")
    print(f"Using content BG: {bg_content}")

    # =========================================================================
    # SLIDE 1: Cover (p)
    # =========================================================================
    print("\n--- Building Slide 1 (Cover) ---")
    # Delete default placeholders i0, i1 first
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "p" --file "{bg_cover}" --x 0 --y 0 --width 720 --height 405')
    ops1 = [
        # Top Google 4-color + Gold Argon strip
        tb("p", "", 0, 0, 180, 3, bg="#4285F4"),
        tb("p", "", 180, 0, 180, 3, bg="#EA4335"),
        tb("p", "", 360, 0, 180, 3, bg="#FBBC04"),
        tb("p", "", 540, 0, 180, 3, bg="#34A853"),

        # Edition Pill
        tb("p", "◆  GOOGLE DEEPMIND // GEMINI 4 ARGON KEYNOTE EDITION", 40, 26, 390, 24, size=9, color="#FBBF24", bg="#1E160B", bold=True, align="center", valign="MIDDLE"),

        # Hero Title
        tb("p", "次世代 AI ペアプログラミングの全貌\nAntigravity × Gemini API CLI", 40, 62, 640, 86, size=29, color="#FFFFFF", bold=True, spacing=120),

        # Subtitle
        tb("p", "自律型エージェントの統合統括、ゼロトラスト境界設計、そしてコマンドライン OS への進化", 40, 154, 640, 24, size=12, color="#CBD5E1"),

        # Bento Card 1: Zero-Trust (with top accent strip)
        tb("p", "", 40, 198, 200, 4, bg="#38BDF8"),
        tb("p", "🔒 ZERO-TRUST\n\n厳格な権限分離モデル\n開発資産と個人領域を保護", 40, 202, 200, 130, size=10.5, color="#E0F2FE", bg="#0C192E", bold=True, align="center", valign="MIDDLE", spacing=135),

        # Bento Card 2: Untethered
        tb("p", "", 260, 198, 200, 4, bg="#F59E0B"),
        tb("p", "📱 UNTETHERED\n\n場所を選ばない遠隔制御\nスマホから監視・即時承認", 260, 202, 200, 130, size=10.5, color="#FEF3C7", bg="#1F160A", bold=True, align="center", valign="MIDDLE", spacing=135),

        # Bento Card 3: 1-Line Multimodal
        tb("p", "", 480, 198, 200, 4, bg="#10B981"),
        tb("p", "⚡ 0-DEPENDENCY\n\n単一バイナリの高速実行\n画像・動画・音声を一撃生成", 480, 202, 200, 130, size=10.5, color="#D1FAE5", bg="#09221B", bold=True, align="center", valign="MIDDLE", spacing=135),

        # Footer
        tb("p", "Presented by aretarumakan  |  GravityNight 2026.10.27  |  Architected with Gemini 4 Argon", 40, 362, 640, 18, size=9, color="#94A3B8", align="center")
    ]
    with open("/tmp/argon_s1.json", "w") as f:
        json.dump(ops1, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s1.json")

    # =========================================================================
    # SLIDE 2: Dual Engine Architecture (Structured Matrix + Synergy Bar)
    # =========================================================================
    print("\n--- Building Slide 2 (Dual Engine) ---")
    s2 = add_blank_slide()
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s2}" --file "{bg_content}" --x 0 --y 0 --width 720 --height 405')
    ops2 = header_ops(s2, "01 // DUAL ENGINE", "「プロジェクト統括」と「専門職人ツール」の役割分担 🤝", "#38BDF8", "#0C192E")
    ops2.extend([
        # Left Column: Antigravity
        tb(s2, "", 40, 60, 305, 3, bg="#38BDF8"),
        tb(s2, "👔 ANTIGRAVITY CORE（統括オーケストレーター）", 40, 63, 305, 30, size=11, color="#38BDF8", bg="#0C192E", bold=True, align="center", valign="MIDDLE"),
        tb(s2, "▸ 状態管理：文脈を保持しプロジェクト全体を設計\n▸ 自律反復：複数ファイル編集・テスト・修正をループ\n▸ 環境統合：Git プッシュやブラウザ実画面検証を代行\n▸ 拡張連携：MCP とスキルで社内・外部ツールを統括", 40, 96, 305, 165, size=10, color="#E2E8F0", bg="#0F172A", spacing=150),
        tb(s2, "🎯 主戦場：アプリ全体の実装・大規模リファクタリング", 40, 265, 305, 28, size=10, color="#7DD3FC", bg="#0B213A", bold=True, align="center", valign="MIDDLE"),

        # Right Column: Gemini API CLI
        tb(s2, "", 375, 60, 305, 3, bg="#10B981"),
        tb(s2, "⚡ GEMINI API CLI（超低遅延・単発マルチモーダル）", 375, 63, 305, 30, size=11, color="#34D399", bg="#09221B", bold=True, align="center", valign="MIDDLE"),
        tb(s2, "▸ 状態管理：過去ログを持たず1行コマンドで最速実行\n▸ 生成能力：画像・動画・音声・構造化JSONを即時出力\n▸ 依存ゼロ：Go言語製の単一静的バイナリでどこでも動作\n▸ パイプ処理：TOON形式・内蔵 jq でスクリプト連携に最適", 375, 96, 305, 165, size=10, color="#E2E8F0", bg="#0F172A", spacing=150),
        tb(s2, "🎯 主戦場：画像・動画・音声の素材生成・高速ログ解析", 375, 265, 305, 28, size=10, color="#6EE7B7", bg="#092920", bold=True, align="center", valign="MIDDLE"),

        # Bottom Architectural Conclusion Bar
        tb(s2, "💡 結論：両者は競合せず、Antigravity（頭脳）が Gemini API CLI（手足）を呼び出すことで開発速度が最大化する", 40, 308, 640, 44, size=10.5, color="#FDE68A", bg="#1F160A", bold=True, align="center", valign="MIDDLE"),
        tb(s2, "Slide 02 / 07", 550, 372, 130, 16, size=8.5, color="#64748B", align="right")
    ])
    with open("/tmp/argon_s2.json", "w") as f:
        json.dump(ops2, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s2.json")

    # =========================================================================
    # SLIDE 3: Zero-Trust Security Boundary
    # =========================================================================
    print("\n--- Building Slide 3 (Zero-Trust) ---")
    s3 = add_blank_slide()
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s3}" --file "{bg_content}" --x 0 --y 0 --width 720 --height 405')
    ops3 = header_ops(s3, "02 // ZERO TRUST", "なぜ Antigravity は Google Workspace に直結しないのか？ 🛡️", "#F43F5E", "#2A0E14")
    ops3.extend([
        # Principle Banner
        tb(s3, "🔒 設計哲学：「繋がらない」のではなく、あえて「直結させない」ゼロトラスト境界モデル\n強力なシェル実行権限を持つ開発エージェントから、個人のメール・全社機密ドキュメントを物理的に隔離", 40, 58, 640, 44, size=10.5, color="#FECDD3", bg="#230C12", bold=True, align="center", valign="MIDDLE", spacing=130),

        # Left Column: 2 Risk Cards
        tb(s3, "⚠️ デフォルト直結が招く 2 大セキュリティリスク", 40, 114, 310, 28, size=11, color="#FB7185", bg="#2A0E14", bold=True, align="center", valign="MIDDLE"),
        tb(s3, "① 機密データの誤コミット・外部流出事故\n個人の Gmail や社内限定ドキュメントを AI が読み取り、\n誤って公開 GitHub リポジトリへ push する致命的リスク。", 40, 146, 310, 96, size=10, color="#E2E8F0", bg="#0F172A", spacing=140),
        tb(s3, "② 過剰権限（Over-Privileged）の危険性\nコード実行・外部通信を行うエージェントに、無条件で\n全社 Google ドライブへのフルアクセス権を渡す危うさ。", 40, 250, 310, 96, size=10, color="#E2E8F0", bg="#0F172A", spacing=140),

        # Right Column: 2 Defense Cards
        tb(s3, "🛡️ MCP × プラグイン分離による正解アプローチ", 370, 114, 310, 28, size=11, color="#34D399", bg="#09221B", bold=True, align="center", valign="MIDDLE"),
        tb(s3, "① 最小権限の原則（Least Privilege）の徹底\n開発者が明示的に許可した機能（例：gslides 等）だけを、\n必要なタイミングのみプラグインとして安全に後付け接続。", 370, 146, 310, 96, size=10, color="#E2E8F0", bg="#0F172A", spacing=140),
        tb(s3, "② オープン規格 MCP によるマルチベンダー対応\n特定クラウドに縛られず、業界標準プロトコル（MCP）で\nGitHub・Slack・DB 等と統一された安全基準で連携。", 370, 250, 310, 96, size=10, color="#E2E8F0", bg="#0F172A", spacing=140),

        tb(s3, "Slide 03 / 07", 550, 372, 130, 16, size=8.5, color="#64748B", align="right")
    ])
    with open("/tmp/argon_s3.json", "w") as f:
        json.dump(ops3, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s3.json")

    # =========================================================================
    # SLIDE 4: Untethered Remote Control
    # =========================================================================
    print("\n--- Building Slide 4 (Remote Control) ---")
    s4 = add_blank_slide()
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s4}" --file "{bg_content}" --x 0 --y 0 --width 720 --height 405')
    ops4 = header_ops(s4, "03 // UNTETHERED", "机からの完全解放！Remote Control のアーキテクチャ 📱", "#A855F7", "#1F1235")
    ops4.extend([
        # Top Relay Flow Bar
        tb(s4, "📱 外出先スマホ (4G/5G)", 40, 58, 190, 32, size=10, color="#E9D5FF", bg="#1F1235", bold=True, align="center", valign="MIDDLE"),
        tb(s4, "⇄  ☁️ Google セキュア中継リレー（同一Wi-Fi不要）  ⇄", 240, 58, 240, 32, size=9.5, color="#FDE68A", bg="#1F160A", bold=True, align="center", valign="MIDDLE"),
        tb(s4, "💻 自宅・社内の Mac 本体", 490, 58, 190, 32, size=10, color="#BAE6FD", bg="#0C192E", bold=True, align="center", valign="MIDDLE"),

        # 3 Pillar Cards
        tb(s4, "", 40, 104, 200, 3, bg="#A855F7"),
        tb(s4, "📶 ANY NETWORK\n別ネットワークから安全直結", 40, 107, 200, 42, size=10.5, color="#E9D5FF", bg="#1F1235", bold=True, align="center", valign="MIDDLE"),
        tb(s4, "Google の暗号化リレーを経由し、\n移動中の 5G 回線やカフェから\n自宅 Mac の開発環境へ安全接続。\n\n重いビルドやテストは Mac に任せ、\nスマホ1つで身軽に移動できます。", 40, 152, 200, 195, size=10, color="#CBD5E1", bg="#0F172A", spacing=145),

        tb(s4, "", 260, 104, 200, 3, bg="#38BDF8"),
        tb(s4, "📱 PURPOSE-BUILT UI\nスマホ専用のカード型画面", 260, 107, 200, 42, size=10.5, color="#BAE6FD", bg="#0C192E", bold=True, align="center", valign="MIDDLE"),
        tb(s4, "PC 画面の縮小コピーではなく、\n思考ログ・差分確認・承認ボタンを\nモバイル画面専用に最適化設計。\n\n「ホーム画面に追加」するだけで、\nネイティブアプリ感覚で即起動！", 260, 152, 200, 195, size=10, color="#CBD5E1", bg="#0F172A", spacing=145),

        tb(s4, "", 480, 104, 200, 3, bg="#F43F5E"),
        tb(s4, "🚨 INSTANT REVOKE\nワンタップで接続トークン破棄", 480, 107, 200, 42, size=10.5, color="#FECDD3", bg="#2A0E14", bold=True, align="center", valign="MIDDLE"),
        tb(s4, "登壇や画面共有中にうっかり\nQR コードが映り込んでしまっても、\n設定を OFF ➔ ON にするだけで\n旧トークンを即座に完全無効化。\n\n第三者の不正接続を 100% 遮断。", 480, 152, 200, 195, size=10, color="#CBD5E1", bg="#0F172A", spacing=145),

        tb(s4, "Slide 04 / 07", 550, 372, 130, 16, size=8.5, color="#64748B", align="right")
    ])
    with open("/tmp/argon_s4.json", "w") as f:
        json.dump(ops4, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s4.json")

    # =========================================================================
    # SLIDE 5: Gemini API CLI Multimodal Showcase (2x2 Bento + robot.jpg)
    # =========================================================================
    print("\n--- Building Slide 5 (Multimodal CLI) ---")
    s5 = add_blank_slide()
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s5}" --file "{bg_content}" --x 0 --y 0 --width 720 --height 405')
    ops5 = header_ops(s5, "04 // MULTIMODAL OS", "Gemini API CLI (v0.4.4) フルマルチモーダル実機検証 ⚡", "#10B981", "#09221B")
    ops5.extend([
        # 2x2 Bento Grid on Left (x=40..405)
        # Card 1: Image (Top-Left)
        tb(s5, "", 40, 60, 178, 3, bg="#38BDF8"),
        tb(s5, "🎨 画像生成 (image)\n$ gemini-api image ...\n\n16:9 や 2K/4K 高解像度に対応。\n数秒でプレゼン素材を直接出力。", 40, 63, 178, 132, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        # Card 2: Video (Top-Right)
        tb(s5, "", 228, 60, 178, 3, bg="#A855F7"),
        tb(s5, "🎬 動画生成 (video)\n$ gemini-api video ...\n\n720p シネマティック MP4 生成。\n縦型動画(9:16)や会話編集に対応。", 228, 63, 178, 132, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        # Card 3: TTS (Bottom-Left)
        tb(s5, "", 40, 208, 178, 3, bg="#F59E0B"),
        tb(s5, "🔊 音声合成 (tts)\n$ gemini-api tts ...\n\n自然な日本語ナレーションを\nWAV 出力し afplay で即座に再生。", 40, 211, 178, 132, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        # Card 4: Analyze (Bottom-Right)
        tb(s5, "", 228, 208, 178, 3, bg="#10B981"),
        tb(s5, "🔍 構造化解析 (analyze)\n$ gemini-api analyze ...\n\nコード・PDF・動画を直接解析。\n内蔵 jq と TOON で省トークン化。", 228, 211, 178, 132, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        # Right Showcase Frame for robot.jpg (x=420, width=260)
        tb(s5, "◆ 実機生成アセット: robot.jpg (2K Output)", 420, 60, 260, 26, size=9.5, color="#FBBF24", bg="#1F160A", bold=True, align="center", valign="MIDDLE"),
        tb(s5, "Prompt: Cute robot coding in a cafe  |  Go Static Binary", 420, 322, 260, 21, size=8.5, color="#94A3B8", bg="#0F172A", align="center", valign="MIDDLE"),

        tb(s5, "Slide 05 / 07", 550, 372, 130, 16, size=8.5, color="#64748B", align="right")
    ])
    with open("/tmp/argon_s5.json", "w") as f:
        json.dump(ops5, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s5.json")
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s5}" --file "{IMG_ROBOT}" --x 420 --y 90 --width 260 --height 228')

    # =========================================================================
    # SLIDE 6: Context Engineering (@Mentions) & Marketplace
    # =========================================================================
    print("\n--- Building Slide 6 (Extensions) ---")
    s6 = add_blank_slide()
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s6}" --file "{bg_content}" --x 0 --y 0 --width 720 --height 405')
    ops6 = header_ops(s6, "05 // ECOSYSTEM", "精度を高める @メンション技術 ＆ マーケットプレイス拡張 🎁", "#F59E0B", "#1F160A")
    ops6.extend([
        # Left Column Header
        tb(s6, "🏷️ 思考精度を劇的に高める @メンション三種の神器", 40, 60, 310, 28, size=10.5, color="#38BDF8", bg="#0C192E", bold=True, align="center", valign="MIDDLE"),
        # 3 Stacked Cards on Left
        tb(s6, "① @conversation（スマート文脈引き継ぎ）\n長期スレッドのノイズを削ぎ落とし、新規スレッドへ\n決定事項と成果物だけを圧縮して引き継ぐリセット技。", 40, 94, 310, 78, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),
        tb(s6, "② @rules（プロジェクト規約の強制適用）\n「日本語コメント必須」「any 禁止」などの開発規約を\nエージェントの行動指針としてワンタッチで注入。", 40, 178, 310, 78, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),
        tb(s6, "③ @file / @folder / @terminal（ピンポイント参照）\n対象コードやターミナルのエラー出力を直接指定し、\n無駄なファイル探索トークンを大幅に節約。", 40, 262, 310, 78, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        # Right Column Header
        tb(s6, "🛍️ Customizations Marketplace と非競合設計", 370, 60, 310, 28, size=10.5, color="#FBBF24", bg="#1F160A", bold=True, align="center", valign="MIDDLE"),
        # 3 Stacked Cards on Right
        tb(s6, "① 「＋」ボタン 1 つで公式プラグインを即導入\nGoogle Docs / Sheets / Slides / Drive / Calendar 等の\n公式拡張を GUI からワンタップで安全に追加可能。", 370, 94, 310, 78, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),
        tb(s6, "② プラグイン（知識）× CLI（道具）の完全分離\nプラグインは「手順書」、CLI は「実行バイナリ」。\nレイヤーが異なるため両方入れても一切混乱しない。", 370, 178, 310, 78, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),
        tb(s6, "③ Google 公式デベロッパーツール群との統合\nFirebase・Chrome DevTools・Flutter 等の専門スキルを\nプロジェクト単位で自在にカスタマイズ可能。", 370, 262, 310, 78, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        tb(s6, "Slide 06 / 07", 550, 372, 130, 16, size=8.5, color="#64748B", align="right")
    ])
    with open("/tmp/argon_s6.json", "w") as f:
        json.dump(ops6, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s6.json")

    # =========================================================================
    # SLIDE 7: Architecture Blueprint & Executive Summary
    # =========================================================================
    print("\n--- Building Slide 7 (Grand Finale) ---")
    s7 = add_blank_slide()
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s7}" --file "{bg_cover}" --x 0 --y 0 --width 720 --height 405')
    ops7 = header_ops(s7, "06 // BLUEPRINT", "Gemini API CLI 全体像 ＆ エグゼクティブ・サマリー 📊", "#F59E0B", "#1F160A")
    ops7.extend([
        # Left Caption for Infographic
        tb(s7, "◆ 実機生成ポスター: infographic_ja.jpg (gemini-api image / 2K)", 40, 56, 430, 22, size=9, color="#38BDF8", bg="#0C192E", bold=True, align="center", valign="MIDDLE"),
        tb(s7, "※ CLI 単発コマンドで生成したアーキテクチャ概念図（Live Generative Proof）", 40, 336, 430, 18, size=8, color="#94A3B8", bg="#0F172A", align="center", valign="MIDDLE"),

        # Right Executive Summary Column (x=485, width=195)
        tb(s7, "", 485, 56, 195, 3, bg="#F59E0B"),
        tb(s7, "📌 KEY TAKEAWAYS\n本日のおさらい", 485, 59, 195, 38, size=10.5, color="#FDE68A", bg="#1F160A", bold=True, align="center", valign="MIDDLE"),
        tb(s7, "1. 適材適所の二刀流\n全体統括は Antigravity、\n単発・高速生成は CLI へ。\n\n2. 安全なゼロトラスト\nWorkspace は直結せず、\nMCP で最小権限のみ接続。\n\n3. 場所と文脈の自由化\nRemote Control で移動中も\n@conversation で快適に開発。", 485, 101, 195, 253, size=9.5, color="#E2E8F0", bg="#0F172A", spacing=135),

        tb(s7, "Slide 07 / 07", 550, 372, 130, 16, size=8.5, color="#64748B", align="right")
    ])
    with open("/tmp/argon_s7.json", "w") as f:
        json.dump(ops7, f, ensure_ascii=False)
    run_cmd(f"gslides mutate batch {PRES_ID} -f /tmp/argon_s7.json")
    run_cmd(f'gslides mutate insert-image-from-file {PRES_ID} --slide "{s7}" --file "{IMG_INFO}" --x 40 --y 80 --width 430 --height 252')

    print("\n=== Argon Edition Presentation Built Successfully! ===")

if __name__ == "__main__":
    main()
