# Plan

Return the exact bytes authenticated by verify_artifact and stage them into a
private controlled generation. Seed npm's content-addressed cache from that
immutable copy before unchanged npm ci. Do not modify the lock or replace any
active generation. Prove fresh-cache offline installation with a real synthetic
npm package, refusal before install when seeding fails, and preservation of the
authenticated bytes if the original input path changes.
