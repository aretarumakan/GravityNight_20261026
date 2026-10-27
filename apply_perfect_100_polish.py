import json
import subprocess
import time

PRES_ID = "1xXP3MwI8Ew9fYXIqLqe5qA9cWuSpFSkdQMxDa7q8Zgs"

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
    path = f"/tmp/batch_polish_{label}.json"
    with open(path, "w") as f:
        json.dump(ops, f, ensure_ascii=False)
    res = subprocess.run(f"gslides mutate batch {PRES_ID} -f {path}", shell=True, capture_output=True, text=True)
    print(f"[{label}] Batch result: {res.stdout.strip() or res.stderr.strip()}")

def main():
    print("=== Applying Perfect 100-Point Polish to Slides 1, 3, 4 ===")

    # 1. Slide 1 Polish (Index 0)
    s1_del = get_elements_to_delete(0)
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

        # 3 Cards (Perfect 3-Line Alignment, Under 17 chars)
        {"op": "add-textbox", "slide": "p", "text": "🔒 100% ZERO-TRUST\n安全な権限分離設計\n開発資産と個人データを厳格分離", "x": 40, "y": 205, "width": 200, "height": 125, "font_size": 11, "bold": True, "color": "#93C5FD", "background_color": "#0E1A33", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},
        {"op": "add-textbox", "slide": "p", "text": "📱 24/7 UNTETHERED\nどこからでも遠隔操作\nスマホからタスク監視・即時承認", "x": 260, "y": 205, "width": 200, "height": 125, "font_size": 11, "bold": True, "color": "#D8B4FE", "background_color": "#1F1235", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},
        {"op": "add-textbox", "slide": "p", "text": "⚡ 1-LINE EXECUTION\n爆速マルチモーダル\n画像・動画・音声をコマンド一撃生成", "x": 480, "y": 205, "width": 200, "height": 125, "font_size": 11, "bold": True, "color": "#6EE7B7", "background_color": "#0A251E", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE", "line_spacing": 140},

        # Footer
        {"op": "add-textbox", "slide": "p", "text": "Presented by aretarumakan  |  GravityNight 2026.10.27  |  Confidential & Proprietary", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "center"}
    ])
    run_batch(ops1, "slide1")
    time.sleep(1)

    # 2. Slide 3 Polish (Index 2)
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

        # Right Card (Protected プラグイン line break)
        {"op": "add-textbox", "slide": sid3, "text": "🛡️ MCP（オープン規格）による正解のアプローチ", "x": 370, "y": 120, "width": 310, "height": 32, "font_size": 11.5, "bold": True, "color": "#34D399", "background_color": "#0A251E", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid3, "text": "• 最小権限の原則 (Least Privilege):\n  開発者が明示許可したスコープのみ、\n  必要な時だけプラグインとして安全接続\n\n• ベンダーロックインの排除:\n  Google だけでなく、業界標準 MCP により自由かつ柔軟なツール連携が可能", "x": 370, "y": 155, "width": 310, "height": 190, "font_size": 11, "color": "#E2E8F0", "background_color": "#0F172A", "line_spacing": 145},

        {"op": "add-textbox", "slide": sid3, "text": "Antigravity Executive Keynote  |  Slide 03", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops3, "slide3")
    time.sleep(1)

    # 3. Slide 4 Polish (Index 3)
    sid4 = "SLIDES_API1240383252_0"
    s4_del = get_elements_to_delete(3)
    ops4 = [{"op": "delete-element", "element": eid} for eid in s4_del]
    ops4.extend([
        {"op": "add-textbox", "slide": sid4, "text": "UNTETHERED", "x": 40, "y": 24, "width": 110, "height": 22, "font_size": 10, "bold": True, "color": "#A855F7", "background_color": "#1F1235", "font_family": "Montserrat", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "机からの完全な解放！Remote Control の技術的革新 📱", "x": 160, "y": 21, "width": 520, "height": 30, "font_size": 16.5, "bold": True, "color": "#F8FAFC", "font_family": "Montserrat", "content_alignment": "MIDDLE"},

        # Card 1 (Protected line break)
        {"op": "add-textbox", "slide": sid4, "text": "📶 ANY NETWORK CONNECT\n同じ Wi-Fi にいなくても OK", "x": 40, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#D8B4FE", "background_color": "#1F1235", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "Google セキュア中継を経由し、外出先のモバイル通信やカフェ Wi-Fi から\n手元の Mac へ安全直結。\n\n重いビルドやテストは Mac に任せ、手ぶらで身軽に移動できます。", "x": 40, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 145},

        # Card 2
        {"op": "add-textbox", "slide": sid4, "text": "📱 PURPOSE-BUILT UI\nスマホ専用のカード型画面", "x": 260, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#38BDF8", "background_color": "#0E1A33", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "PC 画面の単なるミラーではなく、チャット・思考ログ・ファイル変更・承認ダイアログをスマホ専用に最適化。\n\n「ホーム画面に追加」でネイティブアプリ同様にワンタップ起動！", "x": 260, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 145},

        # Card 3
        {"op": "add-textbox", "slide": sid4, "text": "🚨 ONE-CLICK REVOKE\n登壇・配信時も安心の防衛", "x": 480, "y": 70, "width": 200, "height": 45, "font_size": 11, "bold": True, "color": "#F43F5E", "background_color": "#2A0E14", "alignment": "center", "content_alignment": "MIDDLE"},
        {"op": "add-textbox", "slide": sid4, "text": "配信等でうっかり QR コードを見られても、「Enable Remote Control」を OFF ➔ ON でトークン即時破棄。\n\n古いリンクからのアクセスを即座に 100% 無力化できます。", "x": 480, "y": 120, "width": 200, "height": 225, "font_size": 10.5, "color": "#CBD5E1", "background_color": "#0F172A", "line_spacing": 145},

        {"op": "add-textbox", "slide": sid4, "text": "Antigravity Executive Keynote  |  Slide 04", "x": 40, "y": 365, "width": 640, "height": 20, "font_size": 9.5, "color": "#64748B", "alignment": "right"}
    ])
    run_batch(ops4, "slide4")

    print("=== Perfect 100 Polish Completed ===")

if __name__ == "__main__":
    main()
