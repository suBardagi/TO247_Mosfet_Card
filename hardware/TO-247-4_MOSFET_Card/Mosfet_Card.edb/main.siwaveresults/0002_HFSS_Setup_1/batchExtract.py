import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oProject = oDesktop.SetActiveProject(r"main")
oDesign = oProject.SetActiveDesign(r"main")
oDesign.ExportNetworkData("", [r"HFSS Setup 1:HFSS Sweep 1"], 3, r"C:\Users\90541\Desktop\TO247_Mosfet_Card\hardware\TO-247-4_MOSFET_Card\Mosfet_Card.edb\main.siwaveresults\0002_HFSS_Setup_1\main.ts", [ "All" ], True, 50, "S", -1, 0, 15, True)
