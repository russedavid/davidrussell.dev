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
    preview = {"frontline": frontline_preview, "otsc": otsc_preview, "career-workbench": career_preview, "qwen-ttrpg": qwen_preview}
    return Article(
        preview[project["slug"]](),
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

CAREER_WORKBENCH = {
    "slug": "career-workbench", "title": "Career Workbench", "status": "Local web app · Source available",
    "tagline": "A good resume starts before the writing.",
    "description": "Discover overlooked experience, explore directions, and develop profiles whose claims lead back to the original evidence.",
    "stack": "Agentic discovery / Persistent evidence / Document review",
}
PROJECTS.append(CAREER_WORKBENCH)
CAREER_REPO = "https://github.com/russedavid/career-workbench"


def career_preview():
    return Div(
        Div(Span("CAREER WORKBENCH", cls="preview-brand"), Span("Fictional example", cls="preview-label"), cls="preview-bar"),
        Div(P("A contribution, with its context.", cls="report-heading"),
            Blockquote('“I helped keep the volunteer schedule up to date. The program lead owned it.”'),
            P("Supported the weekly volunteer schedule alongside the program lead.", cls="career-example-claim"),
            P("Shared credit preserved · Original account linked", cls="preview-footnote"), cls="career-paper"),
        cls="project-preview career-preview", aria_label="Fictional career evidence with shared ownership preserved in the resulting claim",
    )


CAREER_STEPS = (
    {
        "label": "1. Original account", "status": "Source recorded", "version": "Working profile · draft 1",
        "source": "I coordinated the weekly volunteer schedule for the community program.",
        "claim": "Coordinated the community program’s weekly volunteer schedule.",
        "decision": "Keep the account and its source link. No measured time saving, budget ownership or program size has been supplied.",
        "note": "A source link records where a claim came from; it does not independently verify the recollection.",
    },
    {
        "label": "2. Correction", "status": "Dependent draft needs review", "version": "Draft 1 · historical",
        "source": "I helped keep the schedule up to date. The program lead owned it.",
        "claim": "Coordinated the community program’s weekly volunteer schedule.",
        "decision": "Save the correcting words, retire the overbroad claim, and flag profiles that use it. Preserve the earlier PDF and the account it was based on.",
        "note": "A correction changes the working record; it does not silently rewrite an old export.",
    },
    {
        "label": "3. Revised profile", "status": "Shared contribution retained", "version": "Working profile · draft 2",
        "source": "I helped keep the schedule up to date. The program lead owned it.",
        "claim": "Supported the weekly volunteer schedule alongside the program lead.",
        "decision": "Use the narrower claim in a new draft. Review the wording, inspect the rendered page, and retain both document versions with their source snapshots.",
        "note": "Technical validation and editorial judgment remain separate. A clean PDF can still contain weak copy.",
    },
)


def career_walkthrough(step=0):
    state = CAREER_STEPS[step]
    return Div(
        Div(*(A(item["label"], href=f"/projects/career-workbench?step={index}#walkthrough",
                hx_get=f"/projects/career-workbench/walkthrough/{index}", hx_target="#career-walkthrough", hx_swap="outerHTML",
                cls="walkthrough-step selected" if index == step else "walkthrough-step",
                aria_current="step" if index == step else None) for index, item in enumerate(CAREER_STEPS)),
            cls="walkthrough-controls", role="group", aria_label="Fictional evidence and correction stages"),
        Div(
            Div(P("ORIGINAL WORDS", cls="eyebrow"), Blockquote(state["source"]),
                H3(state["status"]), P(state["decision"]), cls="sample-context"),
            Div(Div(Span(state["version"], cls="preview-brand"), cls="preview-bar"),
                P(state["claim"], cls="career-example-claim" + (" historical-claim" if step == 1 else "")),
                P(state["note"], cls="small-note"), cls="sample-artifact career-artifact"),
            cls="walkthrough-body", aria_live="polite",
        ), id="career-walkthrough", cls="walkthrough",
    )


def career_page(step=0):
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(
            P("Career Workbench / Local web application", cls="eyebrow"),
            H1("A good resume starts before the writing."),
            P("The useful work is often missing from the first account: an unwritten responsibility, a difficult handoff, a decision that helped someone else deliver. Career Workbench helps recover that experience, understand what it supports, and turn it into a clear professional story.", cls="project-lede"),
            Div(A("Get the local app ↗", href=CAREER_REPO + "#run-the-localhost-ui", cls="button-link"),
                A("Read the usage guide ↗", href=CAREER_REPO + "/blob/main/docs/usage.md", cls="text-link"), cls="actions"),
            P("Python · FastHTML · HTMX · SQLite · Codex app-server · MCP · Typst", cls="project-stack"),
            cls="project-hero",
        ),
        Section(
            P("THE PRODUCT", cls="eyebrow"), H2("One working record. Several ways forward."),
            P("Start with notes, a resume or a conversation. The agent can ask a useful follow-up, organize evidence, compare career directions, propose development work, or draft a profile for a particular audience. Direct editors use the same records, so a precise correction does not depend on another model call."),
            Div(
                Div(Span("01", cls="flow-number"), Strong("Discover"), P("Recover overlooked work through short, adaptive interviews.")),
                Div(Span("02", cls="flow-number"), Strong("Make sense of it"), P("Separate contribution, shared credit, outcomes and unknowns.")),
                Div(Span("03", cls="flow-number"), Strong("Choose a direction"), P("Compare evidence gaps and plan work that demonstrates useful capabilities.")),
                Div(Span("04", cls="flow-number"), Strong("Compose and review"), P("Develop distinct profiles, inspect their sources and check the actual PDFs.")),
                cls="context-flow",
            ), cls="case-section",
        ),
        Section(
            P("FOLLOW THE EVIDENCE", cls="eyebrow"), H2("A correction should travel as far as the claim."),
            P("Step through a fictional account, its correction and a revised profile. The important behavior is what happens to the records and drafts that depend on it."),
            career_walkthrough(step),
            P("Fixed, self-authored fictional example. This illustration contains no personal career records and makes no model calls.", cls="small-note"),
            cls="case-section", id="walkthrough",
        ),
        Section(
            P("ENGINEERING DECISIONS", cls="eyebrow"), H2("Let the agent reason. Make the record dependable."),
            detail_row("A frontier model inside a bounded workflow", "Codex supplies the reasoning and tool loop. Workspace-bound MCP tools handle records, corrections and rendering. The host disables general shell and filesystem tools; each conversation resumes its own thread."),
            detail_row("Facts keep their qualifications", "Original sources remain immutable. Claims retain quotation spans, ownership and limitations. A correction retires the old claim and flags dependent profiles and planning records, while historical exports retain their snapshots."),
            detail_row("Large histories stay navigable", "The agent starts with an overview and retrieves selected records in bounded pages. It can inspect a claim and its exact source without loading an entire career archive into every response."),
            detail_row("The rendered page is part of the workflow", "Typst produces tagged PDFs. Checks cover text, metadata, links, fonts, page limits and short wrapped lines; optional bottom-fill and independent PDF/UA validation make additional requirements explicit."),
            detail_row("Progress survives the page", "Background jobs persist visible events, results and failures. Refreshing the browser does not start another model call. Stop requests interrupt model work while retaining changes already saved."),
            cls="case-section",
        ),
        Section(
            P("QUALITY", cls="eyebrow"), H2("Passing a check is a beginning."),
            P("Automated tests exercise source identity, attribution boundaries, corrections, isolated workspaces and document output. Browser checks cover actual forms and review flows in Chromium and Firefox. Separate live exercises use fictional accounts to inspect the agent’s choices and resulting records."),
            P("A quote can be present in a source without supporting the proposed claim. A valid PDF can still tell an unconvincing story. Editorial review therefore considers relevance, coherence, attribution, scope, copy and geometry separately."),
            Div(A("Read the verification notes ↗", href=CAREER_REPO + "/blob/main/docs/web-verification.md", cls="text-link"),
                A("Explore the implementation ↗", href=CAREER_REPO + "/blob/main/docs/design.md", cls="text-link"), cls="actions"),
            cls="case-section",
        ),
        Section(
            P("USE IT LOCALLY", cls="eyebrow"), H2("Your browser is the interface."),
            P("With the prerequisites installed—including an already authenticated Codex CLI—clone the repository and start the web app:"),
            Pre(Code("git clone https://github.com/russedavid/career-workbench.git\ncd career-workbench\nuv sync --frozen\nuv run career-workbench web"), cls="setup-code"),
            P("Open http://127.0.0.1:5010. Create a workspace, add source material, and start a conversation. The README covers dependencies and model selection; the usage guide walks through discovery, drafting, corrections and PDF review."),
            P("Records stay in a private local directory outside the code checkout. Agent conversations use the saved Codex CLI login and send relevant context to the selected model. This is a localhost application, not a hosted public demo.", cls="small-note"),
            cls="case-section",
        ),
        Div(H2("Start with the work. Keep the evidence."),
            P("Explore the fictional examples or bring your own material into a private workspace."),
            Div(A("View the repository ↗", href=CAREER_REPO, cls="button-link"),
                A("Read the usage guide ↗", href=CAREER_REPO + "/blob/main/docs/usage.md", cls="text-link"), cls="actions"),
            cls="project-outro"),
    )


QWEN_REPO = "https://github.com/russedavid/qwen-ttrpg"
DATASET_REPO = "https://github.com/russedavid/format_conversation_dataset"
QWEN_TTRPG = {
    "slug": "qwen-ttrpg", "title": "Qwen TTRPG", "status": "Local model training · Open source tooling",
    "tagline": "Training an AI to take its turn.",
    "description": "A complete path from reviewed conversations to fine-tuned roleplaying assistants: prepare the data, train task adapters, compare their behavior, and serve them locally.",
    "stack": "Conversational data / QLoRA + FSDP2 / Evaluation / GPU serving",
}
PROJECTS.append(QWEN_TTRPG)


def qwen_preview():
    return Div(
        Div(Span("QWEN TTRPG", cls="preview-brand"), Span("Training + inference", cls="preview-label"), cls="preview-bar"),
        Div(P("One shared model", cls="model-base-label"), Strong("27B", cls="model-size"),
            P("Qwen base · three task adapters", cls="model-base-caption"),
            Div(Span("Actions"), Span("Storytelling"), Span("Rules"), cls="adapter-labels"),
            P("Reviewed data → train → verify → compare", cls="preview-footnote"), cls="model-paper"),
        cls="project-preview qwen-preview", aria_label="One 27-billion-parameter Qwen base shared by action, storytelling, and rules adapters",
    )


QWEN_STEPS = (
    {
        "label": "1. Keep the exchange", "status": "A response needs its context",
        "description": "Keep the complete question and the exchange that led to it. Consecutive lines from the responding speaker form one target. Review the wording before it becomes a training example.",
        "context_label": "Prior exchange · input context",
        "context": "Narrator: The ferry is still tied to the dock.\nPlayer: I ask the operator whether we can leave before the storm.",
        "target_label": "Next response · reviewed target",
        "target": "The operator checks the gathering clouds. ‘We can leave now, if you are ready.’ She waits for your answer.",
        "note": "The response addresses the question and leaves the player's decision open.",
    },
    {
        "label": "2. Choose what learns", "status": "Loss belongs to the response",
        "description": "The model sees the full exchange. Only the assistant's response and end-of-turn token contribute to the training loss. Required context and target text are never clipped to squeeze an example into the window.",
        "context_label": "Prompt · excluded from training loss",
        "context": "Narrator: The ferry is still tied to the dock.\nPlayer: I ask the operator whether we can leave before the storm.",
        "target_label": "Completion + end token · included in training loss",
        "target": "The operator checks the gathering clouds. ‘We can leave now, if you are ready.’ She waits for your answer.",
        "note": "Conceptual loss mask. The real build verifies boundaries using the model's own tokenizer.",
    },
    {
        "label": "3. Test the result", "status": "Check the weights, then the behavior",
        "description": "Verify that the saved adapter's tensor names, shapes, and values actually reach the model. Compare the base and adapted model on held-out inputs, then review shuffled answers without candidate identities or timing cues.",
        "context_label": "Same held-out input for both candidates",
        "context": "A new participant question, its preceding exchange, and the established facts. Keep generation settings matched.",
        "target_label": "Questions for the review",
        "target": "Did it answer the latest question?\nDid it preserve what was already established?\nDid it leave the player's choices open?\nDid it invent a fact or rule?",
        "note": "No fabricated model outputs or scores: this step illustrates the comparison protocol.",
    },
)


def qwen_walkthrough(step=0):
    item = QWEN_STEPS[step]
    return Div(
        Div(*(A(state["label"], href=f"/projects/qwen-ttrpg?step={index}#walkthrough",
                hx_get=f"/projects/qwen-ttrpg/walkthrough/{index}", hx_target="#qwen-walkthrough", hx_swap="outerHTML",
                cls="walkthrough-step selected" if index == step else "walkthrough-step",
                aria_current="step" if index == step else None) for index, state in enumerate(QWEN_STEPS)),
            cls="walkthrough-controls", role="group", aria_label="From conversation to model evaluation"),
        Div(
            Div(P("THE TRAINING DECISION", cls="eyebrow"), H3(item["status"]), P(item["description"]), cls="sample-context"),
            Div(
                Div(P(item["context_label"], cls="training-label"), Pre(item["context"]), cls="training-context"),
                Div(P(item["target_label"], cls="training-label"), Pre(item["target"]), cls="training-target"),
                P(item["note"], cls="small-note"), cls="sample-artifact training-example"),
            cls="walkthrough-body", aria_live="polite"),
        id="qwen-walkthrough", cls="walkthrough",
    )


def qwen_page(step=0):
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(
            P("Qwen TTRPG / Local model training and serving", cls="eyebrow"),
            H1("Training an AI to take its turn."),
            P("A player asks a question, changes course, or challenges an assumption. The next response has to meet that moment and carry the story forward. I built a local pipeline to turn conversational context into training examples, fine-tune Qwen, and test what the resulting model actually does.", cls="project-lede"),
            Div(A("Explore the training pipeline ↗", href=QWEN_REPO, cls="button-link"),
                A("See how an example is built ↓", href="#walkthrough", cls="text-link"), cls="actions"),
            P("Qwen3.8-27B · PyTorch · Axolotl · QLoRA · FSDP2 · llama.cpp", cls="project-stack"),
            cls="project-hero",
        ),
        Section(
            P("THE MODEL WORK", cls="eyebrow"), H2("Three jobs. One shared base."),
            P("I fine-tuned task adapters for recognizing game actions, suggesting the next response, and answering questions from supplied rules. Training runs on two 24 GB GPUs with CPU offload. At inference time, the adapters share a quantized base model and are selected per request."),
            Div(
                Div(Span("01", cls="flow-number"), Strong("Prepare"), P("Review responses, preserve their context, and reserve independent sources for evaluation.")),
                Div(Span("02", cls="flow-number"), Strong("Adapt"), P("Train small LoRA weight updates while keeping the large base model frozen.")),
                Div(Span("03", cls="flow-number"), Strong("Verify"), P("Reload the exact tensors, compare behavior, and retain failures for review.")),
                Div(Span("04", cls="flow-number"), Strong("Serve"), P("Route requests to task adapters and measure time to first text and completion.")),
                cls="context-flow",
            ), cls="case-section",
        ),
        Section(
            P("INSIDE A TRAINING EXAMPLE", cls="eyebrow"), H2("The question belongs with the answer."),
            qwen_walkthrough(step),
            P("Fixed, self-authored fictional illustration. It contains no source conversation or model-generated result and makes no inference calls.", cls="small-note"),
            cls="case-section", id="walkthrough",
        ),
        Section(
            P("ENGINEERING DECISIONS", cls="eyebrow"), H2("Follow the evidence all the way to inference."),
            detail_row("The data pipeline is part of the model", "The companion Conversational Dataset Formatter preserves speaker and source provenance, binds reviews to exact response text, and checks for shared sources and repeated targets across training and evaluation splits. Completion-only masks keep the learning objective tied to the intended response."),
            detail_row("Training has to fit the machine", "QLoRA limits trainable parameters; FSDP2 and CPU offload distribute training across the available hardware. Activation checkpointing trades extra computation for memory. The launcher checks GPU availability and records the configuration used for each run."),
            detail_row("A saved adapter must survive the handoff", "Portable export removes checkpoint-wrapper names without altering tensor values. Strict reload compares names, shapes, and loaded values. GGUF conversion checks that attention-head permutations preserve the low-rank weight update."),
            detail_row("Shared weights still have a scheduling cost", "Each inference request enables its task adapter and explicitly disables the others. Reusing one base saves model memory, but different adapter configurations can queue separately. Context length and concurrent requests still compete for GPU memory."),
            cls="case-section",
        ),
        Section(
            P("EVALUATION", cls="eyebrow"), H2("An improvement has to survive a comparison."),
            P("Base and adapted models receive matched inputs and generation settings. The harness records completion status, time to first visible text, total latency, token usage, and explicit response checks. A separate A/B review shuffles candidate labels independently of execution order."),
            P("Lower reference loss does not establish a better response. Review considers relevance, continuity, participant agency, and unsupported facts. The original continuation is one possible answer; a good alternative may use different words."),
            P("The published tools have automated CI checks and have been exercised with the real local tokenizer and model service. The included synthetic cases test the harness; they are not a representative quality benchmark. Training material, fine-tuned weights, and private comparison reports are not distributed.", cls="small-note"),
            Div(A("Read the evaluation protocol ↗", href=QWEN_REPO + "/blob/main/docs/evaluation.md", cls="text-link"),
                A("Inspect the reload checks ↗", href=QWEN_REPO + "/blob/main/qwen_ttrpg/adapters.py", cls="text-link"), cls="actions"),
            cls="case-section",
        ),
        Div(H2("Two repositories. One path from data to deployment."),
            P("Use the formatter to prepare reviewed examples, then train, evaluate, and serve adapters with Qwen TTRPG. Both run locally with your own material and model files. Cloning the code does not download my fine-tuned weights."),
            Div(A("Qwen TTRPG ↗", href=QWEN_REPO, cls="button-link"),
                A("Conversational Dataset Formatter ↗", href=DATASET_REPO, cls="text-link"), cls="actions"),
            cls="project-outro"),
    )
