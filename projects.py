"""Public project descriptions and self-authored product illustrations."""

from fasthtml.common import *

FRONTLINE = {
    "slug": "frontline", "title": "Frontline", "status": "Live web demo",
    "tagline": "Maintenance reports with a paper trail.",
    "description": "Turn notes, recordings, and photos into a maintenance report that keeps observations, completed work, and next steps distinct.",
    "stack": "Multimodal inputs / Retrieval / Evidence review",
}
PROJECTS = [FRONTLINE]


def frontline_preview():
    return Div(
        Div(Span("FRONTLINE", cls="preview-brand"), Span("Example report", cls="preview-label"), cls="preview-bar"),
        Div(P("Gateway inspection", cls="report-heading"),
            Div(Span("COMPLETED", cls="state-label"), P("Reseated the power cable."), cls="report-line"),
            Div(Span("OBSERVED", cls="state-label"), P("Gateway back online."), cls="report-line"),
            Div(Span("UNKNOWN", cls="state-label muted"), P("Power supply rating."), cls="report-line"),
            P("Every claim has a source. Missing facts stay missing.", cls="preview-footnote"), cls="report-paper"),
        cls="project-preview frontline-preview", aria_label="Illustrative Frontline report separating completed work, observations, and unknown values",
    )


def project_card(project):
    return Article(
        frontline_preview(),
        Div(P(project["status"], cls="project-status"), H3(A(project["title"], href=f"/projects/{project['slug']}")),
            P(project["tagline"], cls="project-tagline"), P(project["description"], cls="project-description"),
            P(project["stack"], cls="project-stack"), A("Explore the project →", href=f"/projects/{project['slug']}", cls="text-link"),
            cls="project-copy"), cls="project-card",
    )


def project_section():
    return Section(
        Div(H2("Selected work"), A("All projects →", href="/projects", cls="text-link"), cls="section-heading"),
        Div(*(project_card(project) for project in PROJECTS), cls="project-grid"), id="selected-work",
    )


def detail_row(title, text):
    return Div(H3(title), P(text), cls="decision-row")


def frontline_page():
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(
            P("Frontline / Live web demo", cls="eyebrow"),
            H1("A maintenance report should never invent a repair."),
            P("A planned replacement is not a completed repair. An unreadable label is not a known specification. Frontline turns field evidence into a report while keeping those distinctions visible.", cls="project-lede"),
            Div(A("Try Frontline ↗", href="https://davidrussell.alwaysdata.net", cls="button-link"),
                A("View source ↗", href="https://github.com/russedavid/fastdemo", cls="text-link"), cls="actions"),
            P("Python · FastHTML · HTMX · SQLite FTS5 · Groq", cls="project-stack"), cls="project-hero",
        ),
        Section(
            Div(P("THE INPUT", cls="eyebrow"), H2("Field notes, in their own words."),
                Blockquote('“Pi 4 gateway offline. Reseated the power cable; back online. Supply label is unreadable. Check the supply on the next visit.”'),
                P("The source records a cable adjustment and a recovery. It does not establish that the power supply was replaced—or even what its rating is.", cls="muted"),
                P("Self-authored example illustrating the report structure.", cls="small-note")),
            frontline_preview(), cls="example-grid",
        ),
        Section(
            P("THE WORKFLOW", cls="eyebrow"), H2("From evidence to a reviewable report."),
            Ol(
                Li(Strong("Collect the evidence."), " Add written notes, recordings, and equipment photos to a workspace."),
                Li(Strong("Find applicable guidance."), " Match manufacturer references to the equipment model and revision. Keep that guidance separate from recorded work."),
                Li(Strong("Draft with sources."), " Preserve unknowns and disagreements, attach source references, and separate completed actions from proposals."),
                Li(Strong("Review the result."), " Inspect the evidence beside the report and keep reviewer notes separate from generated findings."),
                cls="workflow-list",
            ), cls="case-section",
        ),
        Section(
            P("ENGINEERING DECISIONS", cls="eyebrow"), H2("The source matters as much as the sentence."),
            detail_row("Evidence that stays put", "A report keeps an immutable source snapshot. Later edits to the workspace do not silently change what an earlier report was based on."),
            detail_row("Retrieval with boundaries", "SQLite FTS5 and BM25 provide a small lexical index. Model, revision, and access checks decide which references are eligible before they reach the model."),
            detail_row("Quality beyond valid JSON", "Structural checks catch malformed fields and invalid source references. Separate trace review looks for invented work, unsupported quantities, and claims the cited passage does not support."),
            detail_row("A demo that can be operated", "Visitor workspaces are isolated, uploads and requests are bounded, and saved work survives process restarts. The public demo runs on alwaysdata with Groq inference."),
            cls="case-section",
        ),
        Section(
            P("EVALUATION", cls="eyebrow"), H2("Make the failures inspectable."),
            P("The development corpus contains 20 synthetic cases. Reviewing paired outputs exposed errors such as moving proposed work into the completed-work section. Revised instructions improved assistant-reviewed passes from 12/20 to 18/20 on those same development examples."),
            P("Those are provisional assistant judgments on a small development set, not human-calibrated accuracy or a customer outcome. The source repository retains the comparisons and remaining failures.", cls="small-note"),
            Div(A("Read the evaluation method ↗", href="https://github.com/russedavid/fastdemo/blob/main/docs/evaluation-method.md", cls="text-link"),
                A("Inspect the retrieval study ↗", href="https://github.com/russedavid/fastdemo/blob/main/docs/reference-retrieval.md", cls="text-link"), cls="actions"),
            cls="case-section",
        ),
        Div(H2("Try a report with its sources attached."),
            P("Open the demo and choose an example, or bring your own notes."),
            A("Open Frontline ↗", href="https://davidrussell.alwaysdata.net", cls="button-link"), cls="project-outro"),
    )
