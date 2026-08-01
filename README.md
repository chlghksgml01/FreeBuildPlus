# FreeBuild Plus

Soulmask building overlay: **snap / support / floating + collision / overlap** in one mod.

Merges the former:
- [FreeBuildNoSnapSupport](https://github.com/chlghksgml01/FreeBuildNoSnapSupport) (`_1_P`)
- [FreeBuildNoCollision](https://github.com/chlghksgml01/FreeBuildNoCollision) (`_2_P`)

| Install | File |
|---|---|
| Overlay | `WS-WindowsNoEditor_1_P.pak` (+ `.sig`) |
| Location | `Soulmask\WS\Content\Paks\` |
| Never touch | `WS-WindowsNoEditor.pak` (base game) |

**Do not** also install the old FreeBuild / NoCollision overlays — use **this pak only**.

---

## What it does

- Mid-air / no nearby support (FreeBuild lane)
- Overlap vs grass, other buildings, decor (collision JianCe lane)
- Structure attach (floor/wall) still works in testing
- Terrain-vs-terrain block may still appear (left intentional)

---

## Install (local test)

1. Unsubscribe / remove old **FreeBuild** and **FreeBuild No Collision** Workshop items if subscribed  
2. Run `mod\INSTALL_OVERLAY.bat` from this mod folder under `WS\Mods\FreeBuildPlus`  
   (or copy `mod\OverlayPaks\WS-WindowsNoEditor_1_P.pak` + `.sig` into `Content\Paks`)  
3. Launch Soulmask **from Steam**  
4. Mods → apply this mod if listed → full restart if prompted  

Uninstall: `mod\UNINSTALL_OVERLAY.bat` (deletes `_1_P` only; never deletes base pak).

---

## Hard rules (from collision postmortem)

1. Never set `bZhiNeng*` = TRUE  
2. Never copy `*JianCeBoxExtent` from native CDO (zeros wipe boxes)  
3. Prefer bool-only collision relax (`bUseCollisionJianCeBox` etc.)  
4. If placement bricks → delete `_1_P` (+`.sig`)

See `docs/LESSONS.md`.

---

## Repo layout

```text
mod/INSTALL_OVERLAY.bat
mod/UNINSTALL_OVERLAY.bat
mod/OverlayPaks/   ← signed overlay (local builds; not always on GitHub LFS)
docs/LESSONS.md
tools/             ← editor patch scripts
```

Cooked assets / `.pak` may be omitted from public git depending on size policy.

---

## License

Scripts/docs: MIT. Soulmask / Epic content is not included.

## Steam Workshop

- **Item (Hidden):** [3775582493](https://steamcommunity.com/sharedfiles/filedetails/?id=3775582493)
- Server arg example: `-mod="3775582493"`
- After subscribe: run `INSTALL_OVERLAY.bat` in `WS\Mods\FreeBuildPlus`
