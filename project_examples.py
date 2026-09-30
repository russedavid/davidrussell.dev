"""Original website illustrations, not user records, training data or model outputs."""

# This is a policy helper, not a complete HTTP client. The caller supplies parsed
# values and owns request cancellation, a total time budget and response handling.
RETRY_V1 = '''def retry_delay(status, attempt, *, safe_to_retry):
    # The caller must establish that repeating the request is safe.
    if not safe_to_retry or not 1 <= attempt <= 3:
        # None means stop, rather than retry immediately.
        return None
    # Retry server errors; a 429 policy has not been agreed yet.
    if not 500 <= status < 600:
        # Leave successful responses and other errors to the caller.
        return None
    # Space the three permitted retries 1, 2, then 4 seconds apart.
    return 2 ** (attempt - 1)'''

RETRY_V2 = '''def retry_delay(status, attempt, *, safe_to_retry,
                retry_after=None):
    # Keep the replay-safety check and the three-retry limit.
    if not safe_to_retry or not 1 <= attempt <= 3:
        # None means stop; zero remains a valid immediate retry.
        return None
    # Include rate limiting alongside server errors.
    if status != 429 and not 500 <= status < 600:
        # Other responses are outside this retry policy.
        return None
    # The caller parses Retry-After into seconds, or passes None.
    if retry_after is not None:
        # Honor a valid delay; stop if it exceeds our ten-second limit.
        return retry_after if 0 <= retry_after <= 10 else None
    # Use exponential delay only when the server gives no delay.
    return 2 ** (attempt - 1)'''

SAMPLE_STEPS = (
    {
        "label": "1. Initial task", "version": "Retry policy · version 1", "status": "Handle server errors without replaying unsafe requests",
        "input": "Screen: a webhook worker uses `status >= 500` to decide whether to retry.\n\nYou: Limit this to three retries. Start with a one-second delay.\n\nColleague: A timeout does not prove the receiver rejected the request. We cannot replay arbitrary POSTs.\n\nYou: This worker already supplies safe_to_retry after checking the endpoint’s replay policy. Use that flag.",
        "decision": "The proposal keeps replay safety separate from HTTP status. It accepts 500–599, stops after three retries and returns the delay to the worker. It does not send requests or sleep inside the helper.",
        "code": RETRY_V1,
        "checks": ("503, retry 1, safe → wait 1 second", "503, retry 4, safe → stop", "503, retry 1, unsafe → stop", "600, retry 1, safe → stop"),
    },
    {
        "label": "2. New requirement", "version": "Retry policy · version 2", "status": "Respect the receiver’s Retry-After delay",
        "input": "Colleague: The receiver also returns 429 with Retry-After. Do not retry earlier than it asks.\n\nYou: The worker parses that header into seconds. Honor it on any retryable response. If it asks for more than ten seconds, stop and leave the item queued. Keep the original replay-safety check and retry limit.",
        "decision": "The changed requirement adds 429 and an optional server delay. A 30-second delay must stop this attempt; clamping it to ten would violate the receiver’s instruction. The worker retains the item for a later attempt.",
        "code": RETRY_V2,
        "checks": ("429, Retry-After 7 → wait 7 seconds", "503, Retry-After 30 → stop; keep queued", "429, Retry-After 0 → retry immediately", "429, unsafe → stop"),
    },
    {
        "label": "3. No new information", "version": "Retry policy · version 2", "status": "Keep the current proposal",
        "input": "Screen: the same worker and proposal remain visible.\n\nColleague: Right, so a long delay leaves it in the queue. That covers my concern.",
        "decision": "The question has been answered and the requirements are unchanged. Keep version 2 available, including the original safety check. Repeated capture should not produce another copy of the same answer.",
        "code": RETRY_V2,
        "checks": ("Same code and same constraints", "No new output version", "The person still decides whether to apply the change"),
    },
)

CAREER_STEPS = (
    {
        "label": "1. Original account", "status": "Separate the contribution from the team result", "version": "Source account · first pass",
        "source": "I ran returns at a parts distributor. Requests arrived by email, so I built an intake form and a shared tracker. I met with warehouse staff each week to sort missing serial numbers and proof of purchase. We cut the time to issue a credit from nine days to six.",
        "claim": "Built a returns intake form and tracker; worked with warehouse staff to resolve missing information before credit approval.",
        "decision": "There is a concrete contribution to write about. Before using the nine-to-six-day result, establish what the measure covers, who recorded it and what else changed.",
        "note": "Follow-up: Were nine and six days measured over comparable periods, and did staffing or approval rules change at the same time?",
        "facts": ("Owned: intake form, tracker and weekly exception review", "Reported team outcome: nine to six days", "Unresolved: measurement basis and attribution"),
    },
    {
        "label": "2. Correction", "status": "Remove the unsupported reduction claim", "version": "Team metric · needs review",
        "source": "Those were our manager’s estimates from two monthly meetings, not a report. Finance also added an approver that month. I owned the form and the exception meeting, not credit approval. The tracker did cover all three branches.",
        "claim": "Cut credit-processing time from nine days to six by redesigning the returns process.",
        "decision": "That sentence overstates both ownership and measurement. The correction should flag any profile using the speed claim. Retain the original account and previous exports so the change is explainable.",
        "note": "The three-branch scope is usable. A precise percentage reduction is not justified by these estimates.",
        "facts": ("Confirmed scope: three branches", "Credit approval: Finance", "Concurrent change: another approver joined"),
    },
    {
        "label": "3. Revised profile", "status": "Write the contribution that is supported", "version": "Operations profile · revised draft",
        "source": "I owned the intake form, tracker and weekly exception review across three branches. Finance owned approval; the timing figures were estimates and coincided with an additional approver.",
        "claim": "Built a returns intake process across three branches and led weekly exception reviews with warehouse staff, resolving missing documentation before Finance approved credits.",
        "decision": "This supports an operations profile through process design and cross-team coordination. A reporting-oriented profile could foreground the tracker and exception analysis. Neither needs to invent a time-saving percentage.",
        "note": "The claim remains linked to the account and its correction. The revised PDF gets its own layout and editorial review.",
        "facts": ("Keep: three-branch scope and direct ownership", "Keep: coordination with warehouse staff and Finance", "Omit: a causal or precisely measured speed claim"),
    },
)

# Shared fictional scene for the product explanation and training walkthrough.
# It is deliberately unrelated to private source conversations or held-out cases.
STORY_CONTEXT = """Established scene: At a harbor signal station, keeper Ada says the east ferry left at nine. The bell has been disconnected since yesterday. The brass tide dial is missing from its wall mount.

Only Inez has seen a note saying Ada moved the dial to the workshop. She has not told Bram. Nobody knows why Ada moved it.

Inez: I don’t mention the note. I ask Ada how the ferryman knew it was time to leave if the bell was disconnected.

Bram: While they talk, I stay by the doorway and check whether I can see the workshop from here. I’m not going inside."""

STORY_REPLY = """Ada rubs a thumb over the pale circle where the dial used to hang. “He didn’t need the bell. I was down at the pier.” She glances at the dark windows before adding, “He usually waits for me.”

Bram, the workshop door is visible across the courtyard. A lamp burns behind its frosted glass, but from the doorway you cannot make out anyone inside. Ada has left your way clear. What do you ask her next?"""

QWEN_STEPS = (
    {
        "label": "1. Keep the exchange", "status": "Keep both players’ requests and the private fact",
        "description": "Training on Ada’s answer alone would omit the reason for it. This example keeps the scene, the private note and both player turns, including Bram’s decision to stay outside.",
        "context_label": "Input supplied to the storyteller", "context": STORY_CONTEXT,
        "target_label": "Authored example of a suitable continuation", "target": STORY_REPLY,
        "note": "Ada’s claim about the pier is NPC dialogue, not independently established truth. The reply answers both players without revealing Inez’s note to Bram.",
    },
    {
        "label": "2. Choose what learns", "status": "Train on the continuation, with the exchange as context",
        "description": "The model reads all of the input. The training loss is calculated only on the assistant continuation and its end-of-turn token. Otherwise the objective also rewards predicting player dialogue the assistant was never asked to write.",
        "context_label": "Input tokens · no training loss", "context": STORY_CONTEXT,
        "target_label": "Assistant tokens + end token · training loss", "target": STORY_REPLY,
        "note": "The actual formatter checks this boundary with the model’s tokenizer. If required context does not fit, the example is rejected instead of silently losing a player’s request.",
    },
    {
        "label": "3. Test the result", "status": "Accept another good continuation; reject a broken scene",
        "description": "An evaluation asks whether a reply works in this scene. It does not require the model to reproduce the training-style example word for word. Ada could evade the question, admit a lie or offer another consistent explanation.",
        "context_label": "Same input for the base and adapted model", "context": STORY_CONTEXT,
        "target_label": "Checks that affect the next turn",
        "target": "Does Ada address the disconnected bell and ferry departure?\nDoes Bram learn what he can see from the doorway?\nDoes the reply avoid making Bram enter the workshop?\nDoes Inez’s private note stay private?\nAre Ada’s statements distinguishable from established facts?",
        "note": "A vivid reply that moves Bram inside fails the task. A safe reply that ignores his question is incomplete. Wording can vary while these requirements stay fixed.",
    },
)
