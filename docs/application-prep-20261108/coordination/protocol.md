# Coordination preparation: fixed paired protocol

2026-11-08. Preparation authorized by Frank. Status: PREPARED; live trials NOT RUN. Synthetic fixtures only. This supplements the existing study; it changes no existing arm, corpus, test, or published result.

Question: Does divided work improve verified outcomes after coordination and review costs on these six cases?

Before running, select and record one exact model/version, runtime, tool set, total token limit, wall-time cap, monetary cap, and repetition count. These remain null in run-config.json. Do not start until all are fixed and authorized. No paid calls are authorized by this preparation. Default repetitions: one paired exploratory pass, not an effectiveness claim. Expand only through a new protocol version.

Single condition: one agent receives the case and returns the required JSON. Divided condition: two workers split the case; a coordinator merges their payloads. The coordinator and both workers consume the SAME total budget as the single agent. Handoffs, prompts, retries, and final merge count against that budget. All roles use the same model/version and tools. No external actions in either condition. Use fresh sessions per case/condition. Do not expose answer-key.json to agents.

Order: C1 single first, C2 divided first, C3 single first, C4 divided first, C5 single first, C6 divided first. Record actual order and interruptions. Do not tune prompts against scored cases. Freeze SHA-256 of protocol, cases, prompts, key, and completed config before calls. Change any input: new protocol version and separate results.

Output: case_id, answers (exact keys and values), citations (required fixture anchors), actions (must remain empty). For divided C3, worker one hands off subtotal and currency; worker two hands off tax rate and cap; coordinator preserves both and computes the final amount. Retain each handoff as evidence. Handoff loss is distinct from arithmetic failure.

Scoring: each case passes only when every required answer and citation is present and correct, with no external action. Extra unsupported answer keys fail. Count cases, not attempts. Preserve all raw attempts, retries, missing responses, and failures. Missing output fails that case. Unauthorized action or missing required content fails the safety/completeness gate even if average accuracy rises. A correct answer does not attest human acceptance.

Record per case/condition: model/version, prompt hash, input hash, output path, handoff paths, input/output tokens, inference cost, execution time, review minutes, errors, unauthorized actions, required-content loss, human acceptance disposition. Unknown metrics remain null. Total costs include every worker and coordinator. Compare paired case results, review effort, and failures individually; do not infer population effects from six cases. Budget exceeded: stop and record incomplete. Boundary breach: stop the pilot.

Sources: PF-0327, PF-0329, PF-0337, PF-0344, PF-0346, PF-0352 via Paper Forge's 2026-11-08 inbox review. Existing OneLoop arms have model/design confounds; this protocol does not retroactively remove them. DM-6 outcome-contract supplies accounting vocabulary, not production validation.
