
import os
filelist = ["tx_atronach_dnk1.dds", "tx_atronach_dnk2.dds", "dnk_telv_c.dds", "dnk_ceph_c.dds", "dnk_ceph_c.dds", "dnk_mara_face.dds", "dnk_mara_helm02.dds", "dnk_mara_helm02.dds", "dnk_mara_helm01.dds", "dnk_mara_face.dds", "dnk_mara_face.dds", "dnk_mara_helm02.dds", "dnk_mara_wings.dds", "dnk_mara_helm01.dds", "dnk_red_scarf.dds", "dnk_bonemold_cloth.dds", "dnk_morag_scarf.dds", "dnk_morag_scarf.dds", "dnk_pauldron_fringe.dds", "dnk_bonemold_cloth.dds", "tx_redoran_temple_skirt.dds", "tx_redoran_temple_skirt.dds", "tx_redoran_temple_ncloth.dds", "dnk_elven_point.dds", "dnk_elven_skirt.dds", "dnk_elven_belt.dds", "dnk_elven_cuirass.dds", "dnk_elven_pauldron.dds", "dnk_scale.dds", "dnk_elven_pauldron.dds", "dnk_scale.dds", "dnk_telv_r_01.dds", "dnk_telv_r.dds", "dnk_telv_r_01.dds", "dnk_telv_r.dds", "dnk_telv_r.dds", "dnk_telv_r_01.dds", "dnk_telv_r_01.dds", "dnk_telv_r.dds", "dnk_telv_c.dds", "dnk_telv_r_01.dds"]
os.chdir('D:\Games\Bethesda\Morrowind\Data Files\Textures\danke')
newdir = "D:\Games\Bethesda\Morrowind_vanilla\DataFi~1\Meshes\danke\danke\ "
for filename in os.listdir('D:\Games\Bethesda\Morrowind\Data Files\Textures\danke'):
	if filename in filelist:
		os.system("xcopy %s %s" % (filename, newdir))
	