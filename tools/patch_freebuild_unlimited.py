# -*- coding: utf-8 -*-
"""
FreeBuild Unlimited — patch all /Game/Blueprints/JianZhu
Merges FreeBuild snap/support/float + collision JianCe off.
Never touch extents; never ZhiNeng True; never NoTerrain kitchen-sink.
"""
from __future__ import print_function
import unreal
import traceback

LOG_PATH = "C:/SMTemp/FreeBuildUnlimited/patch_unlimited_log.txt"
ROOT = "/Game/Blueprints/JianZhu"

BOOL_FALSE = [
    "bUseCollisionJianCeBox",
    "bFilterCollisionJianCeResult",
    "bUsesKuoZhanJianCeBox",
    "bUsesKuoZhanJianCeBox2",
    "bUseJueSeJianCeBox",
    "bBuildingJianCeAroundJianZhuNum",
    "bZhiNengBuildOnShuWuTree",
    "bZhiNengBuildOnTerrain",
    "bZhiNengBuildUnderWater",
    "bZhiNengBuildInShiNei",
    "bForceHookToMaoDian",
    "bXuYaoZhiChengDiJiInHookChain",
    "bXuYaoZhiChengDiJiInHookChainZ",
    "bCheckZhiChengWhenHooked",
    "bUseZhiChengJianCeBox",
    "bJianCeMultiZhiCheng",
    "bCheckGuanJieWhenHooked",
]
BOOL_TRUE = [
    "bForceBuildWhenFloating",
]
FLOAT_HUGE = [
    "MaxNearbyZhiChengDiJiDistance",
    "MaxNearbyZhiChengDiJiDistanceZ",
    "MaxJianZhuHookDistance",
]
TARGET = 1000000.0

OUT = []
STATS = {"scanned": 0, "with_comp": 0, "patched": 0, "saved": 0, "failed": 0, "skipped": 0}


def log(m):
    OUT.append(str(m))
    try:
        unreal.log("[UNLIMITED] " + str(m))
    except Exception:
        pass


def flush():
    open(LOG_PATH, "w", encoding="utf-8").write("\n".join(OUT) + "\n")


def safe_get(o, n):
    try:
        return True, o.get_editor_property(n)
    except Exception as e:
        return False, str(e).splitlines()[0][:100]


def safe_set(o, n, v):
    try:
        o.set_editor_property(n, v)
        return True
    except Exception:
        return False


def is_building_comp(c):
    try:
        return "JianZhuBuilding" in c.get_class().get_name()
    except Exception:
        return False


def mark_dirty(o):
    try:
        if hasattr(o, "modify"):
            o.modify()
    except Exception:
        pass
    try:
        p = o.get_outermost()
        if p is not None and hasattr(p, "set_dirty_flag"):
            p.set_dirty_flag(True)
        return p
    except Exception:
        return None


def apply(comp):
    ch = False
    for n in BOOL_FALSE:
        ok, before = safe_get(comp, n)
        if not ok:
            continue
        if safe_set(comp, n, False):
            log("    %s: %r -> False" % (n, before))
            ch = True
    for n in BOOL_TRUE:
        ok, before = safe_get(comp, n)
        if not ok:
            continue
        if safe_set(comp, n, True):
            log("    %s: %r -> True" % (n, before))
            ch = True
    for n in FLOAT_HUGE:
        ok, before = safe_get(comp, n)
        if not ok:
            continue
        if safe_set(comp, n, float(TARGET)):
            log("    %s: %r -> %s" % (n, before, TARGET))
            ch = True
    return ch


def main():
    log("==== FreeBuild Unlimited patch (all JianZhu) ====")
    ar = unreal.AssetRegistryHelpers.get_asset_registry()
    try:
        ar.search_all_assets(True)
    except Exception:
        pass
    assets = list(ar.get_assets_by_path(ROOT, recursive=True))
    log("assets=%d" % len(assets))
    pkgs = []
    for a in assets:
        STATS["scanned"] += 1
        try:
            path = str(a.get_editor_property("package_name"))
        except Exception:
            path = str(a.package_name)
        bp = unreal.load_asset(path)
        if bp is None:
            STATS["failed"] += 1
            continue
        try:
            gen = bp.get_editor_property("generated_class")
        except Exception:
            gen = None
        if gen is None:
            try:
                gen = bp.generated_class()
            except Exception:
                gen = None
        if gen is None:
            leaf = path.split("/")[-1]
            gen = unreal.load_object(None, path + "." + leaf + "_C")
        if gen is None:
            STATS["skipped"] += 1
            continue
        cdo = unreal.get_default_object(gen)
        try:
            comps = list(cdo.get_components_by_class(unreal.ActorComponent) or [])
        except Exception:
            comps = []
        targets = [c for c in comps if is_building_comp(c)]
        if not targets:
            STATS["skipped"] += 1
            continue
        STATS["with_comp"] += 1
        log("PATCH %s" % path)
        anyc = False
        for c in targets:
            if apply(c):
                anyc = True
            mark_dirty(c)
        try:
            scs = bp.get_editor_property("simple_construction_script")
            nodes = scs.get_editor_property("all_nodes") if scs else None
            if nodes:
                for node in nodes:
                    try:
                        tmpl = node.get_editor_property("component_template")
                    except Exception:
                        tmpl = None
                    if tmpl is not None and is_building_comp(tmpl):
                        if apply(tmpl):
                            anyc = True
                        mark_dirty(tmpl)
        except Exception:
            pass
        mark_dirty(cdo)
        pkg = mark_dirty(bp)
        if anyc:
            STATS["patched"] += 1
            if pkg:
                pkgs.append(pkg)
        if STATS["patched"] % 50 == 0:
            flush()

    seen = set()
    uniq = []
    for p in pkgs:
        try:
            k = p.get_path_name()
        except Exception:
            k = id(p)
        if k in seen:
            continue
        seen.add(k)
        uniq.append(p)
    log("Saving %d" % len(uniq))
    ok = unreal.EditorLoadingAndSavingUtils.save_packages(uniq, only_dirty=False)
    log("save -> %s" % ok)
    if ok:
        STATS["saved"] = len(uniq)
    log("STATS %s" % STATS)
    log("==== done ====")
    flush()


try:
    main()
except Exception:
    log("FATAL:\n%s" % traceback.format_exc())
    flush()
    raise
