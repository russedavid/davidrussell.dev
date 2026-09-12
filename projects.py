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
        frontline_preview() if project["slug"] == "frontline" else otsc_preview(),
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
                A("View source ↗", href="https://github.com/russedavid/report-generator", cls="text-link"), cls="actions"),
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
            Div(A("Read the evaluation method ↗", href="https://github.com/russedavid/report-generator/blob/main/docs/evaluation-method.md", cls="text-link"),
                A("Inspect the retrieval study ↗", href="https://github.com/russedavid/report-generator/blob/main/docs/reference-retrieval.md", cls="text-link"), cls="actions"),
            cls="case-section",
        ),
        Div(H2("Try a report with its sources attached."),
            P("Open the demo and choose an example, or bring your own notes."),
            A("Open Frontline ↗", href="https://davidrussell.alwaysdata.net", cls="button-link"), cls="project-outro"),
    )

OTSC = {
    "slug": "otsc", "title": "Over The Shoulder Coder", "status": "Mac desktop app · In development",
    "tagline": "An AI collaborator for work in progress.",
    "description": "Follow the screen and the conversation, keep track of changing requirements, and propose code, explanations, diffs, or designs.",
    "stack": "Continuous context / Structured outputs / Native controls",
}
PROJECTS.append(OTSC)


def otsc_preview():
    return Div(
        Div(Span("OTSC", cls="preview-brand"), Span("Illustrative task view", cls="preview-label"), cls="preview-bar"),
        Div(Div(Span("Code", cls="mini-tab selected"), Span("Explanation", cls="mini-tab"), Span("Changes", cls="mini-tab"), cls="mini-tabs"),
            P("Handle the empty case. Keep fractional results.", cls="task-brief"),
            Pre(Code("def average(values):\n    if not values:\n        return 0\n    return sum(values) / len(values)")),
            P("A useful answer. Room for the next requirement.", cls="preview-footnote"), cls="assistant-paper"),
        cls="project-preview otsc-preview", aria_label="Illustrative OTSC view with task context and a proposed average function",
    )


SAMPLE_STEPS = (
    {
        "label": "1. Initial task", "version": "Code · version 1", "status": "New proposal",
        "input": "You: An empty list should return zero.\nOther participant: Keep fractional averages; don't round them.",
        "decision": "Add an empty-input guard while keeping ordinary division. The other participant's constraint belongs in the implementation.",
        "code": "# Compute an average without losing fractional results.\ndef average(values):\n    # Handle the empty list before dividing.\n    if not values:\n        # The requested value for an empty input is zero.\n        return 0\n    # Ordinary division preserves fractional averages.\n    return sum(values) / len(values)",
    },
    {
        "label": "2. New requirement", "version": "Code · version 2", "status": "Proposal revised",
        "input": "You: Some readings are None. Ignore those.\nOther participant: A real zero still needs to count.",
        "decision": "Exclude only None, so valid zero readings remain in the average. The existing empty-input behavior also covers an all-missing list.",
        "code": "# Average the available readings, including real zeros.\ndef average(values):\n    # Exclude missing readings without dropping zero.\n    samples = [v for v in values if v is not None]\n    # Check whether any usable readings remain.\n    if not samples:\n        # Keep the agreed empty-input result.\n        return 0\n    # Divide by the number of available readings.\n    return sum(samples) / len(samples)",
    },
    {
        "label": "3. No new information", "version": "Code · version 2", "status": "Current output retained",
        "input": "Screen: The same code is still visible.\nOther participant: Okay, that makes sense.",
        "decision": "No new requirement, unanswered question, or meaningful code change. Keep version 2 visible instead of generating another answer or history entry.",
    },
)


def otsc_walkthrough(step=0):
    item = SAMPLE_STEPS[step]
    return Div(
        Div(*(A(state["label"], href=f"/projects/otsc?step={index}#walkthrough",
                hx_get=f"/projects/otsc/walkthrough/{index}", hx_target="#otsc-walkthrough", hx_swap="outerHTML",
                cls="walkthrough-step selected" if index == step else "walkthrough-step",
                aria_current="step" if index == step else None) for index, state in enumerate(SAMPLE_STEPS)),
            cls="walkthrough-controls", role="group", aria_label="Sample session stages"),
        Div(
            Div(P("WHAT CHANGED", cls="eyebrow"), Pre(Code(item["input"]), cls="sample-input"),
                H3(item["status"]), P(item["decision"]), cls="sample-context"),
            Div(Div(Span(item["version"], cls="preview-brand"), Span("Proposed code", cls="preview-label"), cls="preview-bar"),
                Pre(Code(item.get("code", SAMPLE_STEPS[1]["code"])), cls="sample-code"),
                P("Teaching comments explain the proposal; the desktop app also offers clean copy.", cls="small-note"),
                cls="sample-artifact"), cls="walkthrough-body", aria_live="polite",
        ), id="otsc-walkthrough", cls="walkthrough",
    )


def otsc_page(step=0):
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(
            P("Over The Shoulder Coder / Mac desktop app", cls="eyebrow"),
            H1("An AI collaborator for work in progress."),
            P("The code is on your screen. A requirement comes up in conversation. Someone challenges an assumption. OTSC brings those signals into one evolving task and helps create the next version of the work.", cls="project-lede"),
            Div(A("Explore a sample session ↓", href="#walkthrough", cls="button-link"),
                A("View source ↗", href="https://github.com/russedavid/over-the-shoulder", cls="text-link"),
                A("See the controller firmware ↗", href="https://github.com/russedavid/k0-max-midi", cls="text-link"), cls="actions"),
            P("Python · AppKit · Screen and audio context · Model orchestration", cls="project-stack"),
            cls="project-hero",
        ),
        Section(
            P("FOLLOW THE TASK", cls="eyebrow"), H2("New information earns a new answer."),
            P("Step through a small coding task. A new requirement changes the proposal; a repeated screen and an acknowledgment do not."),
            otsc_walkthrough(step),
            P("Interactive illustration with fixed, self-authored inputs and responses. This page does not run the desktop app, capture your screen or audio, or call a model.", cls="small-note"),
            cls="case-section", id="walkthrough",
        ),
        Section(
            P("THE SYSTEM", cls="eyebrow"), H2("Keep context moving. Keep output under control."),
            Div(
                Div(Span("01", cls="flow-number"), Strong("Observe"), P("Screen readings + separate microphone and system-audio transcripts")),
                Div(Span("02", cls="flow-number"), Strong("Build context"), P("Source-linked notes, constraints, and observed file fragments")),
                Div(Span("03", cls="flow-number"), Strong("Review the task"), P("Decide whether to answer and whether the output plan needs to change")),
                Div(Span("04", cls="flow-number"), Strong("Propose"), P("Quick guidance, then deeper code, diffs, explanations, or images")),
                cls="context-flow",
            ),
            P("Screen reading, transcription, and context building run independently. Each answer uses a fixed snapshot, so late work cannot overwrite a different task. Browsing an older artifact freezes that view without freezing the rest of the system."),
            cls="case-section",
        ),
        Section(
            P("ENGINEERING DECISIONS", cls="eyebrow"), H2("Useful assistance has to respect what it knows."),
            detail_row("An observed fragment stays a fragment", "Visible code, spoken descriptions, inferred notes, and verified files are different evidence. The app preserves their sources and completeness instead of inventing a full repository from a screenshot."),
            detail_row("The task chooses the output", "A planning pass defines the instructions and named output sections. An algorithm might need code and complexity analysis; a design task might need an image and component explanations. Meaningful task changes can revise that structure."),
            detail_row("Proposals you can inspect", "Source-backed diffs show current and proposed code with line numbers. Teaching comments stay separate from clean copy. The app proposes changes; it does not apply them to your project."),
            detail_row("Conversation affects the work", "Questions and suggestions from other people can change the artifact or warrant a reply. Microphone and system audio remain separate channels; those channel roles are context cues, not verified voice identification."),
            detail_row("Controls that leave your shortcuts alone", "A MIDI keypad handles history, output types, capture, and window placement without taking over editor shortcuts. Click-through makes the pane background transparent while keeping its text readable."),
            cls="case-section",
        ),
        Section(
            P("RELIABILITY WORK", cls="eyebrow"), H2("A good draft is no use if it never arrives."),
            P("Recorded-input evaluation exposed a delivery defect: optional file metadata could cause an otherwise usable answer to be discarded. Separating those validation paths made all 18 stored deep drafts deliverable, up from 9, with their original code preserved."),
            P("That comparison measures delivery behavior, not whether every answer was correct. Perception, task understanding, and usefulness are evaluated separately, with source media, rejected drafts, and provisional reference answers available in the local review interface."),
            P("A later 48-trial planning experiment tested combining context building and plan review. It reduced model calls but made fresh answers slower when the background worker was busy. The independent architecture remains the default."),
            cls="case-section",
        ),
        Div(
            H2("Built around the work already in front of you."),
            P("OTSC is an actively developed Mac desktop application. Its source is public; recorded evaluation traces remain private."),
            Div(A("Revisit the sample session ↑", href="#walkthrough", cls="button-link"),
                A("View source ↗", href="https://github.com/russedavid/over-the-shoulder", cls="text-link"),
                A("Explore the MIDI firmware ↗", href="https://github.com/russedavid/k0-max-midi", cls="text-link"), cls="actions"),
            cls="project-outro",
        ),
    )
