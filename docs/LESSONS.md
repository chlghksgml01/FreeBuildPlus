# FreeBuild Unlimited — lessons (merged)

Unified overlay of FreeBuildNoSnapSupport + FreeBuildNoCollision.

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
