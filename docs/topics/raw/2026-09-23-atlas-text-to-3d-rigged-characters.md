Atlas (text-to-3D) — merged source file. Two reports, 11 days apart.

--- REPORT 2, pasted by jay 2026-09-23 (the reason this card was rewritten) ---

The GTA 6 beach house, rebuilt in Unreal with 44 engine-ready assets.

All 44 came off one Atlas canvas. Concept image in, image to 3D, remesh to a tri budget, bake,
export. 30 meshes landed at <5,000 tris, structural pieces at <1,000, each one with .blend, GLB
and 2K baked maps.

--- REPORT 1, the original basis of this card (jay, 2026-09-12) ---

A text-to-3D tool whose pitch is that it does not stop at a static mesh: a prompt yields a
standardized T-pose plus a rig and skin weights, so the character is IK-ready and animatable the
moment it is generated.

--- END PASTED CONTENT ---

NOTES ON SOURCING (written on the merge, 2026-09-23)

NOT verified by me: both reports. I did not use Atlas, did not see the 44 assets, did not open a
.blend or a GLB, and did not confirm that the pipeline description or the triangle counts are the
vendor's own wording or a user's. No screenshots or links accompanied either paste.

Reported in report 2: 44 engine-ready assets from one canvas; the step order concept image →
image-to-3D → remesh to a tri budget → bake → export; 30 meshes under 5,000 triangles; structural
pieces under 1,000; each asset delivered as .blend + GLB + 2K baked maps.

The card's own arguments, labelled as such in the body:
 1. That report 2 does NOT test the claim this card was originally filed to test. The original
    question was rig quality — topology, joint placement, skin weights. A beach house has no
    skeleton. Environment props exercise the static-mesh path, which the original card called the
    easy part. The card's open question stays open.
 2. That "remesh to a tri budget" is the load-bearing phrase, because it makes the budget an
    INPUT rather than post-hoc cleanup, and that this — not the asset count — is the advance.
 3. That "bake" is doing the visual work: baked 2K maps are how a sub-1,000-triangle wall reads as
    detailed, which is the standard high-to-low bake, automated.
 4. That "engine-ready" is a claim about import, not about scene performance, and that the report
    omits the fields that decide the latter: UV layout quality, whether the 44 assets share a
    texture atlas or carry 44 separate 2K sets, LODs, collision meshes, material/shader setup,
    and lightmap UVs.
 5. That the format list (.blend + GLB + 2K maps) is the durable part, per
    lerobot-the-format-outlives-the-framework.

Neutral note recorded rather than argued: the subject is a rebuild of another studio's art, so the
demo is evidence about the tool's throughput and not about anything shippable.

Naming collision, carried over from the original card: this Atlas is not FastLane's Atlas
(execution abstraction / MEV) referenced elsewhere in this catalogue.

Related items: vibe-modeling-blender-mcp (#109), lerobot-the-format-outlives-the-framework.
