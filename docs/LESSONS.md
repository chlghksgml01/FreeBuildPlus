# FreeBuild Plus — lessons (merged)

Unified overlay of FreeBuildNoSnapSupport + FreeBuildNoCollision.

Formerly named FreeBuild Unlimited.

## Single pak

Use **only** `WS-WindowsNoEditor_1_P.pak`.  
Do not stack old `_2_P` NoCollision or a second FreeBuild overlay.

## Recipe (safe)

**FreeBuild lane (FALSE unless noted):**

- `bForceHookToMaoDian` false  
- `bXuYaoZhiChengDiJiInHookChain` / `Z` false  
- `bCheckZhiChengWhenHooked` false  
- `bUseZhiChengJianCeBox` false  
- `bJianCeMultiZhiCheng` false  
- `bCheckGuanJieWhenHooked` false  
- `bForceBuildWhenFloating` **true**  
- `MaxNearbyZhiChengDiJiDistance` / `Z` / `MaxJianZhuHookDistance` → large  

**Collision lane (FALSE):**

- `bUseCollisionJianCeBox`  
- `bFilterCollisionJianCeResult`  
- `bUsesKuoZhanJianCeBox` / `2`  
- `bUseJueSeJianCeBox`  
- `bBuildingJianCeAroundJianZhuNum`  
- all `bZhiNeng*`  

**Never:** zero extents from native CDO; `FitEverythingNoTerrain` / `NoZhiBei` kitchen-sink; `bZhiNeng* = true`.

## Split-mod history

Local backups before merge:  
`C:\SMTemp\Backups\FreeBuild_split_before_Unlimited_*`

Former repos (GitHub may still exist): FreeBuildNoSnapSupport, FreeBuildNoCollision.

## Wall-hung rotation glitch (2026-08)

Reports: wall torch / hanging firebowl / wall oil lamps / specimen heads placed on wrong axis (90° tilt) while overlay installed.

**Cause:** FreeBuild Plus snap/support relax applied to `Lighting` + `BiaoBen` (and similar wall-hook pieces).

**Test fix (v1.0.3 local):** rebuild `_1_P` **excluding** cooked folders `Lighting` and `BiaoBen` so those assets fall back to vanilla.  
Pak ~9.67 MB / 1716 entries (was ~9.82 MB / 1804). Already installed to local `Content\Paks` for testing.

Tradeoff: those wall décor pieces lose FreeBuild Plus free-place/collision relax until a smarter per-flag restore.
