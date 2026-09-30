"""Project descriptions, recorded measurements and labelled authored illustrations."""

import json
from pathlib import Path

from fasthtml.common import *
from project_examples import CAREER_STEPS, QWEN_STEPS, SAMPLE_STEPS, STORY_CONTEXT, STORY_REPLY

PROSE_STUDY = json.loads((Path(__file__).parent / "assets/data/storyteller-prose-results.json").read_text())
CAREER_REPO = "https://github.com/russedavid/career-workbench"
QWEN_REPO = "https://github.com/russedavid/qwen-ttrpg"
DATASET_REPO = "https://github.com/russedavid/format_conversation_dataset"
STORY_REPO = "https://github.com/russedavid/story-copilot"
OTSC_REPO = "https://github.com/russedavid/over-the-shoulder"
FRONTLINE_REPO = "https://github.com/russedavid/report-generator"

FRONTLINE = {
    "slug": "frontline", "title": "Frontline", "status": "Hosted demo",
    "description": "Draft maintenance reports from field notes, recordings and photos. Review the source for a finding, check applicable equipment guidance, and distinguish a completed repair from a suggested next step.",
    "stack": "FastHTML · Groq · SQLite FTS5 / BM25",
}
OTSC = {
    "slug": "otsc", "title": "Over The Shoulder", "status": "macOS application",
    "description": "Get help while working in an editor, cloud console or browser terminal. The app reads the screen and listens to the conversation, then proposes code, explanations or diagrams. You operate the tools and apply the changes.",
    "stack": "Python / AppKit · Screen and audio processing",
}
CAREER_WORKBENCH = {
    "slug": "career-workbench", "title": "Career Workbench", "status": "Local web application",
    "description": "Work through career research and resume drafts with an agent that can ask follow-up questions and use saved evidence. Correct a source account and see which claims and profiles need another review.",
    "stack": "FastHTML · Codex / MCP · SQLite · Typst",
}
QWEN_TTRPG = {
    "slug": "qwen-ttrpg", "title": "Qwen training tools", "status": "Local GPU training and serving",
    "description": "Prepare conversational training data, train task-specific LoRAs, and compare them with the base model. I use these tools for Story Copilot on two RTX 3090s; the repos support running the same process with your own data.",
    "stack": "PyTorch · QLoRA / FSDP2 · llama.cpp",
}
STORY_COPILOT = {
    "slug": "story-copilot", "title": "Story Copilot", "status": "Local web application",
    "description": "Suggest the game facilitator’s next reply using the conversation, scenario and character sheets. It can look up an earlier exchange or a supplied rule before answering. Suggestions stay private and do not become recorded events.",
    "stack": "Local models · Evidence tools · Conversation memory",
}
PROJECTS = [FRONTLINE, OTSC, CAREER_WORKBENCH, QWEN_TTRPG, STORY_COPILOT]


def detail_row(title, text):
    return Div(H3(title), P(text), cls="decision-row")


def preview_line(label, text):
    return Div(Span(label, cls="state-label"), P(text), cls="report-line")


def training_feature():
    return Section(
        Div(P("Model training", cls="eyebrow"), H2("Fine-tuning the Story Copilot model"),
            P("For Story Copilot, I trained a model to respond to players in a tabletop game. It needs to answer their questions, remember who knows what, and leave their decisions to them."),
            P("The latest adapter wrote much shorter replies, but did not clearly beat the base model on the separate test. The write-up covers the data, training setup, comparison and remaining failures."),
            A("Read the training results →", href="/projects/qwen-ttrpg#prose-study", cls="text-link")),
        Div(Div(Strong("1,250"), Span("reviewed training exchanges")),
            Div(Strong("27B"), Span("parameters in the base model")),
            Div(Strong("2 × 3090"), Span("local training hardware")), cls="study-stats"),
        cls="training-feature", aria_label="Story Copilot fine-tuning experiment",
    )


def frontline_preview():
    return Div(
        Div(Span("FRONTLINE", cls="preview-brand"), Span("Authored report excerpt", cls="preview-label"), cls="preview-bar"),
        Div(P("Intermittent gateway outage", cls="report-heading"),
            preview_line("WORK", "Reseated the DC connector. The spare supply was not installed."),
            preview_line("CHECK", "216 queued readings uploaded; reporting continued during a five-minute check."),
            preview_line("FOLLOW-UP", "Verify the supply rating. The photographed label is unreadable."),
            P("The work order requested a replacement; the visit note says it did not happen.", cls="preview-footnote"), cls="report-paper"),
        cls="project-preview", aria_label="Authored maintenance example with a requested replacement that was not performed",
    )


def otsc_preview():
    return Div(
        Div(Span("OVER THE SHOULDER", cls="preview-brand"), Span("Authored task excerpt", cls="preview-label"), cls="preview-bar"),
        Div(P("Changing a webhook retry policy", cls="report-heading"),
            preview_line("SCREEN", "A worker retries responses with status >= 500."),
            preview_line("AUDIO", "“Handle 429 too. Honor Retry-After, but stop if it exceeds ten seconds.”"),
            preview_line("PROPOSAL", "Preserve replay safety and retry limits. A long server delay leaves the item queued."),
            P("The walkthrough shows the code change and the cases it must handle.", cls="preview-footnote"), cls="report-paper"),
        cls="project-preview", aria_label="Authored screen-and-conversation example about retry timing and replay safety",
    )


def career_preview():
    return Div(
        Div(Span("CAREER WORKBENCH", cls="preview-brand"), Span("Fictional account", cls="preview-label"), cls="preview-bar"),
        Div(P("Who changed the returns process?", cls="report-heading"),
            preview_line("ACCOUNT", "“I built the intake form and tracker across three branches.”"),
            preview_line("CORRECTION", "“Finance also added an approver. The timing figures were estimates.”"),
            preview_line("DRAFT", "Describe the process and coordination work; omit the unsupported speed claim."),
            cls="report-paper"), cls="project-preview career-preview",
        aria_label="Fictional career example separating a person's contribution from a team timing estimate",
    )


def qwen_preview():
    test = PROSE_STUDY["splits"]["test"]
    return Div(
        Div(Span("QWEN TRAINING", cls="preview-brand"), Span("Recorded test result", cls="preview-label"), cls="preview-bar"),
        Div(P("Base model vs. prose adapter", cls="report-heading"),
            preview_line("BASE", f"{test['arms']['base']['outcomes']['pass']} pass · 8 fail · 5 uncertain"),
            preview_line("ADAPTER", f"{test['arms']['s1250']['outcomes']['pass']} pass · 9 fail · 1 uncertain"),
            preview_line("PREFERENCE", "19 for each model, with 2 ties."),
            P("40 cases, one response per model per case. Assistant judgments; no human calibration.", cls="preview-footnote"), cls="report-paper"),
        cls="project-preview", aria_label="Actual 40-case test comparison; no clear preference for the fine-tuned model",
    )


def story_preview():
    return Div(
        Div(Span("STORY COPILOT", cls="preview-brand"), Span("Authored scene excerpt", cls="preview-label"), cls="preview-bar"),
        Div(P("At the harbor signal station", cls="report-heading"),
            preview_line("INEZ", "Questions Ada about a ferry departure. Keeps a private note to herself."),
            preview_line("BRAM", "Checks the view of the workshop from the doorway; stays outside."),
            preview_line("REPLY", "Give Ada an answer and Bram an observation, without disclosing the note or moving him inside."),
            cls="report-paper"), cls="project-preview", aria_label="Authored scene with two player requests and separate character knowledge",
    )


def project_card(project):
    previews = {"frontline": frontline_preview, "otsc": otsc_preview, "career-workbench": career_preview,
                "qwen-ttrpg": qwen_preview, "story-copilot": story_preview}
    return Article(
        Div(P(project["status"], cls="project-status"),
            H3(A(project["title"], href=f"/projects/{project['slug']}")),
            P(project["description"], cls="project-description"),
            P(project["stack"], cls="project-stack"), cls="project-copy"),
        previews[project["slug"]](),
        Div(A("How it works →", href=f"/projects/{project['slug']}", cls="text-link"), cls="project-card-link"),
        cls="project-card",
    )


def project_section():
    return Section(
        Div(H2("Projects"), A("All project pages →", href="/projects", cls="text-link"), cls="section-heading"),
        P("Applications and model tools I’m building. Each page explains the implementation, shows an example, and links the code and evaluation findings.", cls="project-section-intro"),
        Div(*(project_card(project) for project in PROJECTS), cls="project-grid"), id="selected-work",
    )


def frontline_page():
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(P("Frontline / Hosted demo", cls="eyebrow"), H1("Maintenance reports from notes, photos and recordings"),
            P("A technician’s notes mix symptoms, work performed and things to check next time. Frontline assembles a report from that material and lets the reviewer inspect the sources. It also retrieves applicable equipment guidance without treating the manual as evidence that a repair happened.", cls="project-lede"),
            Div(A("Open the demo ↗", href="https://davidrussell.alwaysdata.net", cls="button-link"), A("Source code ↗", href=FRONTLINE_REPO, cls="text-link"), cls="actions"),
            P(FRONTLINE["stack"], cls="project-stack"), cls="project-hero"),
        Section(P("Example visit", cls="eyebrow"), H2("The work order and the visit note disagree"),
            P("The work order requests a power-supply replacement for an intermittently offline gateway. The technician returns with these records:"),
            Dl(Dt("Work order"), Dd("Replace the gateway power supply; inspect the intermittent outage."),
               Dt("Voice note · 09:18"), Dd("Reseated the DC connector. The gateway came back and uploaded 216 queued readings. Brought a spare supply but did not install it."),
               Dt("Follow-up note · 09:23"), Dd("Readings continued at the expected one-minute interval during the five-minute check. Verify the existing supply rating before choosing a replacement."),
               Dt("Photo description"), Dd("The gateway is identified as a Raspberry Pi 4. The supply label is too worn to read its rating."), cls="example-sources"),
            frontline_preview(),
            P("The report can describe the reconnection and the short observation period. It cannot conclude that the supply was replaced, that its rating is correct, or that the outage is permanently resolved."),
            P("Authored scenario and report excerpt, not output from a recorded application run.", cls="small-note"), cls="case-section"),
        Section(H2("How the report is assembled"),
            detail_row("Prepare the inputs", "Audio and image interpretation become reviewable source material alongside written notes. The report saves the exact source snapshot used for that attempt, so later edits do not rewrite its history."),
            detail_row("Select references", "SQLite FTS5 and BM25 rank passages from a small equipment library. Model, revision and access filters run before selection. Reference guidance is stored separately from the technician’s observations and completed work."),
            detail_row("Check the draft", "The app checks required fields and source references. A separate review looks for interpretation errors: an action filed under the wrong section, an unsupported quantity, or a cited passage that does not support the sentence."),
            detail_row("Keep the hosted demo usable", "Uploads, requests and storage are bounded. Visitor workspaces are isolated, and saved work survives process restarts. The demo uses alwaysdata and Groq."), cls="case-section"),
        Section(H2("What the development evaluation found"),
            P("Reviewing 20 authored cases found that reports sometimes described proposed work as completed work. Revised instructions raised assistant-reviewed passes from 12/20 to 18/20 on the same development cases. Two interpretation errors remained."),
            P("A separate retrieval study checked whether the selected passage applied to the equipment in the notes. The revised policy found a relevant top passage in 12/12 answerable cases and abstained in eight unsupported cases, but extra passages still introduced irrelevant material. These are small development studies with assistant judgments, not independently measured customer outcomes."),
            Div(A("Report evaluation ↗", href=FRONTLINE_REPO + "/blob/main/docs/evaluation-method.md", cls="text-link"),
                A("Retrieval comparison ↗", href=FRONTLINE_REPO + "/blob/main/docs/reference-retrieval.md", cls="text-link"), cls="actions"), cls="case-section"),
    )


def otsc_walkthrough(step=0):
    item = SAMPLE_STEPS[step]
    return Div(
        Div(*(A(state["label"], href=f"/projects/otsc?step={i}#walkthrough", hx_get=f"/projects/otsc/walkthrough/{i}",
                hx_target="#otsc-walkthrough", hx_swap="outerHTML", cls="walkthrough-step selected" if i == step else "walkthrough-step",
                aria_current="step" if i == step else None) for i, state in enumerate(SAMPLE_STEPS)),
            cls="walkthrough-controls", role="group", aria_label="Retry-policy changes"),
        Div(Div(P("Screen and conversation", cls="eyebrow"), Pre(item["input"], cls="sample-input"),
                H3(item["status"]), P(item["decision"]), H4("Expected behavior"), Ul(*(Li(c) for c in item["checks"])), cls="sample-context"),
            Div(Div(Span(item["version"], cls="preview-brand"), cls="preview-bar"), Pre(Code(item["code"]), cls="sample-code"),
                P("Python policy helper. The worker supplies parsed header values and owns cancellation, queue persistence and the total time budget. This is not a complete HTTP retry client.", cls="small-note"),
                P("Comments explain the decisions. The desktop app also provides a clean copy without teaching comments.", cls="small-note"), cls="sample-artifact"),
            cls="walkthrough-body", aria_live="polite"), id="otsc-walkthrough", cls="walkthrough",
    )


def otsc_page(step=0):
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(P("Over The Shoulder / macOS", cls="eyebrow"), H1("An assistant that follows your screen and conversation"),
            P("OTSC helps while you work in an editor, cloud console or browser-based SSH session. It reads screenshots and listens to separate microphone and system-audio channels, then suggests code, explanations, diffs or diagrams. You continue to operate the tools; the assistant does not need access to the remote machine’s shell or files.", cls="project-lede"),
            Div(A("View the example ↓", href="#walkthrough", cls="button-link"), A("Source code ↗", href=OTSC_REPO, cls="text-link"), cls="actions"),
            P(OTSC["stack"], cls="project-stack"), cls="project-hero"),
        Section(H2("How OTSC handles a changing retry policy"),
            P("A colleague adds a requirement while you are editing a webhook worker. The assistant needs to incorporate it without losing the earlier safety constraint. Step through the conversation and resulting code proposal."),
            otsc_walkthrough(step),
            P("Authored illustration, informed by the app’s task-continuity tests. The code is checked locally; these are not recorded model responses. This page captures no screen or audio and makes no model calls.", cls="small-note"), cls="case-section", id="walkthrough"),
        Section(H2("Capture and answers run independently"),
            P("Screen reading and audio transcription continue while an answer is being generated. A context worker records new constraints, resolves corrections and keeps track of visible code fragments. The answer uses a fixed snapshot of that context."),
            P("When the task changes, a planning pass can change the output sections: code and an explanation for one task, a checklist or diagram for another. Repeated observations that add no useful information should keep the existing answer. You can hold an older artifact on screen while capture continues."),
            detail_row("Code read from a screenshot", "The app keeps the excerpt, its source observation and known line positions. A spoken description cannot establish file contents. If you explicitly connect a local project, verified file snapshots provide a stronger basis for diffs."),
            detail_row("A proposed edit", "The host calculates the diff against the observed or selected source. It shows what would be added or removed without applying the edit. Missing optional file metadata should not discard an otherwise useful answer."),
            detail_row("Questions from another person", "A question about replay safety belongs in the task, even if it comes from system audio. Channel labels help distinguish participants, but are not proof of speaker identity."), cls="case-section"),
        Section(H2("A source-mapping failure found by evaluation"),
            P("In the native workflow study, OCR read a function correctly but included the editor’s line-number gutter. The context worker returned the code without those numbers. A literal-source check rejected the mismatch, so the user received a code proposal without its companion diff."),
            P("The fix records exact source regions and derives code and line positions from the gutter. A fresh replay recovered the observed file and diff for both failing screenshots. Those were two synthetic screens; they do not establish general OCR accuracy."),
            P("The same workflow study exercised changing requirements, another participant’s question, duplicate suppression and a delayed answer arriving after a task reset. It also distinguished an answer being generated from that answer becoming visible in the currently selected pane."),
            Div(A("Workflow findings ↗", href=OTSC_REPO + "/blob/main/docs/task-continuity-results.md", cls="text-link"),
                A("Source-mapping fix ↗", href=OTSC_REPO + "/blob/main/docs/ocr-source-mapping.md", cls="text-link"), cls="actions"), cls="case-section"),
        Section(H2("Desktop controls"),
            P("The output pane can stay visible with a nearly transparent background and opaque text. Click-through, history controls and an optional MIDI keypad let you move through suggestions without taking over normal keyboard shortcuts."),
            A("Controller mappings and firmware ↗", href="https://github.com/russedavid/k0-max-midi", cls="text-link"), cls="case-section"),
    )


def career_walkthrough(step=0):
    state = CAREER_STEPS[step]
    return Div(
        Div(*(A(item["label"], href=f"/projects/career-workbench?step={i}#walkthrough", hx_get=f"/projects/career-workbench/walkthrough/{i}",
                hx_target="#career-walkthrough", hx_swap="outerHTML", cls="walkthrough-step selected" if i == step else "walkthrough-step",
                aria_current="step" if i == step else None) for i, item in enumerate(CAREER_STEPS)),
            cls="walkthrough-controls", role="group", aria_label="Fictional returns-coordinator account and correction"),
        Div(Div(P("Source account", cls="eyebrow"), Blockquote(state["source"]), H3(state["status"]), P(state["decision"]), cls="sample-context"),
            Div(P(state["version"], cls="preview-brand"),
                P(state["claim"], cls="career-example-claim" + (" historical-claim" if step == 1 else "")),
                Ul(*(Li(fact) for fact in state["facts"])), P(state["note"], cls="small-note"), cls="sample-artifact career-artifact"),
            cls="walkthrough-body", aria_live="polite"), id="career-walkthrough", cls="walkthrough",
    )


def career_page(step=0):
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(P("Career Workbench / Local web application", cls="eyebrow"), H1("Career research and resume drafting in a local workspace"),
            P("Career Workbench helps a person recover experience, compare career directions and write resumes from a saved record of their work. The agent can ask follow-up questions, inspect sources, edit claims and render a profile. The same records are editable in the browser.", cls="project-lede"),
            Div(A("Run the app locally ↗", href=CAREER_REPO + "#run-the-localhost-ui", cls="button-link"), A("Usage guide ↗", href=CAREER_REPO + "/blob/main/docs/usage.md", cls="text-link"), cls="actions"),
            P(CAREER_WORKBENCH["stack"], cls="project-stack"), cls="project-hero"),
        Section(H2("An example with shared credit and an uncertain metric"),
            P("A returns coordinator has a useful process-improvement story, but the first account combines their work with a team timing estimate. The follow-up establishes what they owned and what the numbers can support."),
            career_walkthrough(step),
            P("Fixed, self-authored fictional example. It is not a customer record or a recorded model response.", cls="small-note"), cls="case-section", id="walkthrough"),
        Section(H2("How the agent works with the record"),
            detail_row("Discovery and research", "The agent uses the current account to choose a follow-up question or an evidence lookup. It can compare possible directions and suggest work to fill a gap. A planned project stays distinct from a demonstrated accomplishment."),
            detail_row("Corrections", "Sources are preserved. Correcting a claim marks dependent profiles and planning records for review, including indirect dependencies. Previous exports retain the sources and wording they used."),
            detail_row("Tools and persistence", "Codex provides the model-directed loop. MCP tools are scoped to one workspace; general shell and filesystem access are disabled. Chats, jobs and completed changes persist across browser refreshes and interrupted runs."),
            detail_row("PDF review", "Typst renders the profile with fixed templates. The app checks text, fonts, metadata, page limits and short wrapped lines. The reviewer can inspect the page and each claim’s source; passing geometry checks does not judge the writing."), cls="case-section"),
        Section(H2("What has been exercised"),
            P("Chromium and Firefox checks cover uploads, structured editing, interviews, background rendering and PDF review. Separate live Codex exercises use fictional accounts to inspect tool choices and saved records. They verify an application workflow, not career outcomes."),
            A("Verification notes ↗", href=CAREER_REPO + "/blob/main/docs/web-verification.md", cls="text-link"), cls="case-section"),
        Section(H2("Run the localhost UI"),
            P("With the prerequisites installed, including an already authenticated Codex CLI:"),
            Pre(Code("git clone https://github.com/russedavid/career-workbench.git\ncd career-workbench\nuv sync --frozen\nuv run career-workbench web"), cls="setup-code"),
            P("Open http://127.0.0.1:5010, create a workspace and add source material. The app uses the saved Codex login. Relevant context is sent to the selected model; local records and exports stay in a private directory outside the code checkout."), cls="case-section"),
    )


def qwen_walkthrough(step=0):
    item = QWEN_STEPS[step]
    return Div(
        Div(*(A(state["label"], href=f"/projects/qwen-ttrpg?step={i}#walkthrough", hx_get=f"/projects/qwen-ttrpg/walkthrough/{i}",
                hx_target="#qwen-walkthrough", hx_swap="outerHTML", cls="walkthrough-step selected" if i == step else "walkthrough-step",
                aria_current="step" if i == step else None) for i, state in enumerate(QWEN_STEPS)),
            cls="walkthrough-controls", role="group", aria_label="Training context, loss mask and response evaluation"),
        Div(Div(H3(item["status"]), P(item["description"]),
                P(item["context_label"], cls="training-label"), Pre(item["context"], cls="sample-input"), cls="sample-context"),
            Div(Div(P(item["target_label"], cls="training-label"), Pre(item["target"]), cls="training-target"),
                P(item["note"], cls="small-note"), cls="sample-artifact training-example"), cls="walkthrough-body", aria_live="polite"),
        id="qwen-walkthrough", cls="walkthrough",
    )


def prose_study():
    rows = []
    for split, label in [("validation", "Validation"), ("test", "Separate test")]:
        for arm, name in [("base", "Untuned base"), ("s1250", "1,250-example LoRA")]:
            counts = PROSE_STUDY["splits"][split]["arms"][arm]["outcomes"]
            rows.append(Tr(Th(label + " · " + name, scope="row"), Td(counts["pass"]), Td(counts["fail"]), Td(counts["uncertain"])))
    return Section(
        H2("Results of the 1,250-example run"),
        P("The latest run trained a fresh prose adapter for 4 hours 39 minutes on two 24 GB GPUs. I compared it with the untuned base on 40 validation cases, then a separate 40-case test. Each model produced one answer per case."),
        P("The adapter was preferred in validation: 24 comparisons to 13, with three ties. On the separate test, preference was tied at 19 each, with two ties. The result did not establish an overall storytelling improvement."),
        Div(Table(Caption("Assistant-reviewed outcomes · September 2026"),
                  Thead(Tr(Th("Split / model", scope="col"), Th("Pass", scope="col"), Th("Fail", scope="col"), Th("Uncertain", scope="col"))),
                  Tbody(*rows)), cls="results-table"),
        P("The replies became much shorter: a median of 18.5 words on the test, compared with 159.5 from the base. Some improved by dropping unnecessary narration. Others lost part of the player’s request. Definite failures rose from eight to nine, even as the number of passes increased."),
        P("Median generation time fell from 7.47 to 1.90 seconds, largely because there was less text to generate. Validation loss also fell, from 2.608 to 2.017. Neither measurement resolves whether a person would find the next reply useful. The adapter remains experimental and is available in the private application for hands-on testing."),
        Details(Summary("Review method and limits"),
            P("Review checked whether the answer addressed the current request, preserved established facts and uncertainty, respected player choices and handled mechanics appropriately. A consistent new fictional detail was allowed; reproducing the reference continuation was not required."),
            P("All 80 scenarios were audited and independently cross-reviewed using Astra High before the run. The final answer reviewer was an assistant, with model identities hidden until each split’s grades were saved. It had previously seen reference continuations, so this was not a fully independent assessment. No human calibration was performed."),
            P("The cases come from four source families and include related characters and situations. There was one generation per case. This measures the writer with prepared context, not transcription accuracy or the complete live copilot."),
            A("Aggregate measurements ↗", href="/public/data/storyteller-prose-results.json", cls="text-link")),
        cls="case-section", id="prose-study",
    )


def qwen_page(step=0):
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(P("Qwen training tools", cls="eyebrow"), H1("Fine-tuning Qwen for Story Copilot"),
            P("Story Copilot needs to suggest the next reply in a tabletop game. A useful answer responds to the players, respects what their characters know, and leaves unresolved choices open. I built the data, training and evaluation tools to investigate whether a local model could do this better after fine-tuning.", cls="project-lede"),
            Div(A("Training source code ↗", href=QWEN_REPO, cls="button-link"), A("Latest results ↓", href="#prose-study", cls="text-link"), cls="actions"),
            P("Qwen3.8-27B · QLoRA / FSDP2 · Two RTX 3090s · llama.cpp", cls="project-stack"), cls="project-hero"),
        Section(H2("What changed in the training task"),
            P("Earlier versions asked the storyteller to produce a structured object containing narration and other fields. I separated the jobs: the writer now returns prose, while another model extracts state changes from what the participants actually said. A suggested reply never becomes part of the recorded conversation on its own."),
            P("The data work then focused on complete responses to other speakers. An isolated narrator line is often a poor training target: the model needs the question, the relevant facts and any restriction on what a character knows. Reviews keep those connections and exclude uncertain boundaries or overlapping targets."), cls="case-section"),
        Section(H2("An example of the context and training target"),
            P("In this invented scene, one player has a private clue and another has explicitly chosen to stay outside a room. The next reply must address both players without losing either condition."),
            qwen_walkthrough(step),
            P("Fixed, self-authored fictional illustration. These passages explain the data contract; they are not private training excerpts, benchmark cases or generated model answers.", cls="small-note"), cls="case-section", id="walkthrough"),
        prose_study(),
        Section(H2("Training and serving on two GPUs"),
            detail_row("Fit the training job", "QLoRA learns small weight updates while the quantized base stays frozen. FSDP2, CPU offload and activation checkpointing let the 27B training job run on two 24 GB cards with 128 GB of host RAM. Recomputing activations and moving data to RAM trade time for memory."),
            detail_row("Check the exact training input", "The dataset formatter checks source groups, repeated targets and the model’s own chat-template boundaries. Only the response and its end token contribute to loss. Required context is not silently cut to fit a token limit."),
            detail_row("Verify the saved adapter", "After training, the loader checks tensor names, shapes and values against the exported adapter. Conversion to GGUF checks that attention-head rearrangement preserves the low-rank update. A file existing on disk is not enough to show the model is using the intended weights."),
            detail_row("Share the base at inference", "The classifier, rules, storyteller and player adapters use the same quantized base. Each request enables its adapter and disables the others. This saves model memory, but requests can still queue and longer context still needs more memory."), cls="case-section"),
        Section(H2("Earlier SFT, DPO and agent-RL experiments"),
            P("I also compared supervised recipes and direct preference optimization (DPO) for the earlier structured writer. Preference training improved some editorial judgments but did not fix the reliability problems. Those scores use a different response contract and should not be combined with the prose experiment into one learning curve."),
            P("A separate 4B model learned evidence decisions through supervised warm-up and GRPO reinforcement learning. On 36 authored scenarios at two seeds, it passed 66/72 attempts versus 56/72 after the same number of extra supervised updates. The checks concerned conclusions and citations, not storytelling. The RL extension took about twice as long; matching update counts did not match compute."),
            Div(A("SFT and DPO findings ↗", href=QWEN_REPO + "/blob/main/docs/storyteller-preference-results.md", cls="text-link"),
                A("Agent RL study ↗", href=QWEN_REPO + "/blob/main/docs/agent-rl-results.md", cls="text-link"), cls="actions"), cls="case-section"),
        Section(H2("Run the process with your own data"),
            P("The public repositories provide data preparation, training, reload checks, conversion, comparison reports and local serving. They include authored fixtures for exercising the tools. My training material, generated review traces and fine-tuned weights remain private."),
            Div(A("Qwen training toolkit ↗", href=QWEN_REPO, cls="button-link"), A("Dataset formatter ↗", href=DATASET_REPO, cls="text-link"), A("Story Copilot application →", href="/projects/story-copilot", cls="text-link"), cls="actions"), cls="case-section"),
    )


def story_page():
    return (
        A("← All projects", href="/projects", cls="back-link"),
        Section(P("Story Copilot / Local web application", cls="eyebrow"), H1("Private suggestions for a tabletop-game facilitator"),
            P("Story Copilot follows the conversation and suggests what the facilitator could say next. It can consult the scenario, character sheets, earlier exchanges and rules supplied for the game. The facilitator can use a reply, reject it or ask for another. Only the actual conversation updates the record.", cls="project-lede"),
            Div(A("Run it locally ↗", href=STORY_REPO + "#start-locally", cls="button-link"), A("Source code ↗", href=STORY_REPO, cls="text-link"), cls="actions"),
            P("FastHTML · SQLite · Local models · Optional audio intake", cls="project-stack"), cls="project-hero"),
        Section(H2("A scene with two requests and a private clue"),
            Div(Div(H3("Conversation and established facts"), Pre(STORY_CONTEXT, cls="sample-input")),
                Div(H3("A possible facilitator reply"), Blockquote(STORY_REPLY),
                    P("This gives Inez an answer from Ada and Bram a view from the doorway. It leaves the note private and does not decide that Bram enters the workshop. Ada’s account of the departure can still be a lie.")), cls="scene-example"),
            P("Authored scene and suggested reply, not a recorded model result. It illustrates the behavior the application is intended to support; actual responses can fail these requirements.", cls="small-note"), cls="case-section"),
        Section(H2("How the application prepares a reply"),
            detail_row("Follow what was actually said", "Typed contributions and optional audio transcripts feed the conversation record. A separate extractor proposes state updates. The prose writer sees relevant context; its drafts are not fed back as observed events."),
            detail_row("Retrieve or ask before answering", "A bounded agent loop can inspect a character, recover an exchange or search the campaign’s rule documents. When information is missing, it can ask a question. Rule calculations use explicit inputs and verified arithmetic."),
            detail_row("Handle corrections and long sessions", "Revising a contribution invalidates dependent observations and obsolete answers. The context builder preserves complete exchanges and relevant state within a measured token budget. Sessions can continue from existing history or branch into a separate version."),
            detail_row("Review the suggestion", "A separate editing pass checks a draft for continuity, knowledge and player-agency problems. The original and any revision remain in the trace. This adds latency and can over-restrict a reply; it needs evaluation too."), cls="case-section"),
        Section(H2("The local models"),
            P("The main 27B base serves task-specific adapters. Two experimental player-personality adapters can take labelled turns using only the character’s permitted context. Their reference loss improved, but small blind writing comparisons were mixed."),
            P("A separate 4B learned policy handles supported resource and numerical-rule questions. The larger model handles broader decisions, writing and review, and takes over if the smaller policy fails or its context is too large."),
            P("The latest 1,250-example prose writer is available for private interactive testing. Its separate test preference tied the base model. A real UI request verified the new routing, but the reviewer flagged that first reply; integration success did not make it a good answer."),
            Div(A("Storyteller training results →", href="/projects/qwen-ttrpg#prose-study", cls="text-link"), A("Player adapter study ↗", href=QWEN_REPO + "/blob/main/docs/player-results.md", cls="text-link"), cls="actions"), cls="case-section"),
        Section(H2("Workflow failures found in testing"),
            P("The application tests cover source revisions, stale answers, private knowledge, rule isolation and session continuation. Live exercises also follow conversation through transcription, extraction, retrieval and suggestions."),
            P("Audio replay exposed a fragmented question and a review pass that restored an obsolete resource balance. Another review found invented retrospective commentary in private notes. Those failures matter even when the response has valid structure and correct-looking citations."),
            P("Synthetic speech supports repeatable integration tests. Retained natural speech supplies a different stress case. Without an independently corrected transcript and speaker reference, neither supports a word-error or diarization-accuracy claim."),
            A("Workflow evaluation and findings ↗", href=STORY_REPO + "/blob/main/docs/evaluation.md", cls="text-link"), cls="case-section"),
    )
