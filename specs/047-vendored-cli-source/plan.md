# Plan

Return the exact bytes authenticated by verify_artifact and stage them into a
private controlled generation. Seed npm's content-addressed cache from that
immutable copy before unchanged npm ci. Do not modify the lock or replace any
active generation. Prove fresh-cache offline installation with a real synthetic
npm package, refusal before install when seeding fails, and preservation of the
authenticated bytes if the original input path changes.

For the shared-consumer amendment, add keyword-only root context to both public
entrypoints and source authorization, retaining standalone default behavior.
Prove real consumer pin/corpus selection, unchanged operator precedence, forged
pin refusal and invalid consumer-root refusal before package work. Preserve all
193 existing assertions; consuming wrappers get separate real transport tests.
