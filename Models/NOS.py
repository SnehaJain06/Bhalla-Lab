import moose

moose.Neutral('/model')
moose.CubeMesh('/model/kinetics')

#Groups

moose.Neutral('/model/kinetics/Ca_g')
moose.Neutral('/model/kinetics/CaM_g')
moose.Neutral('/model/kinetics/CaMKII_g')
moose.Neutral('/model/kinetics/PP1_g')
moose.Neutral('/model/kinetics/NO_g')
moose.Neutral('/model/kinetics/HN_g')
moose.Neutral('/model/kinetics/DR_g')
moose.Neutral('/model/kinetics/Ap_g')

#Ca_g molecules

NMDA = moose.Pool('/model/kinetics/Ca_g/NMDA')
NMDAinfo = moose.Annotator(NMDA.path+'/info')

NMDAR = moose.Pool('/model/kinetics/Ca_g/NMDAR')
NMDARinfo = moose.Annotator(NMDAR.path+'/info')

Glu = moose.Pool('/model/kinetics/Ca_g/Glu')
Gluinfo = moose.Annotator(Glu.path+'/info')

Glu_bindNMDAR = moose.Reac('/model/kinetics/Ca_g/Glu_bindNMDAR')
Glu_bindNMDARinfo = moose.Annotator(Glu_bindNMDAR.path+'/info')

Ca_influx = moose.Reac('/model/kinetics/Ca_g/Ca_influx')
Ca_influxinfo = moose.Annotator(Ca_influx.path+'/info')

Ca = moose.Pool('/model/kinetics/Ca_g/Ca')
Cainfo = moose.Annotator(Ca.path+'/info')

#Ca_g connections

moose.connect('/model/kinetics/Ca_g/Glu_bindNMDAR','sub','/model/kinetics/Ca_g/NMDA','reac')
moose.connect('/model/kinetics/Ca_g/Glu_bindNMDAR','sub','/model/kinetics/Ca_g/Glu','reac')
moose.connect('/model/kinetics/Ca_g/Glu_bindNMDAR','prd','/model/kinetics/Ca_g/NMDAR','reac')
moose.connect('/model/kinetics/Ca_g/Ca_influx','sub','/model/kinetics/Ca_g/NMDAR','reac')
moose.connect('/model/kinetics/Ca_g/Ca_influx','prd','/model/kinetics/Ca_g/Ca','reac')

#Ca_g parameters

moose.element('/model/kinetics/Ca_g/NMDA').concInit = 120.0
moose.element('/model/kinetics/Ca_g/Glu').concInit = 100.0
moose.element('/model/kinetics/Ca_g/NMDAR').concInit = 0.0
moose.element('/model/kinetics/Ca_g/Ca').concInit = 0.0
moose.element('/model/kinetics/Ca_g/Glu_bindNMDAR').Kf = 50.7
moose.element('/model/kinetics/Ca_g/Glu_bindNMDAR').Kb = 1.179
moose.element('/model/kinetics/Ca_g/Ca_influx').Kf = 1.234
moose.element('/model/kinetics/Ca_g/Ca_influx').Kb = 8.133


#CaM_g molecules

CaM = moose.Pool('/model/kinetics/CaM_g/CaM')
CaMinfo = moose.Annotator(CaM.path+'/info')

CaM_bindCa = moose.Reac('/model/kinetics/CaM_g/CaM_bindCa')
CaM_bindCainfo = moose.Annotator(CaM_bindCa.path+'/info')

CaM_Ca = moose.Pool('/model/kinetics/CaM_g/CaM_Ca')
CaM_Cainfo = moose.Annotator(CaM_Ca.path+'/info')

CaM_Ca_bindCa = moose.Reac('/model/kinetics/CaM_g/CaM_Ca_bindCa')
CaM_Ca_bindCainfo = moose.Annotator(CaM_Ca_bindCa.path+'/info')

CaM_Ca2 = moose.Pool('/model/kinetics/CaM_g/CaM_Ca2')
CaM_Ca2info = moose.Annotator(CaM_Ca2.path+'/info')

CaM_Ca2_bindCa = moose.Reac('/model/kinetics/CaM_g/CaM_Ca2_bindCa')
CaM_Ca2_bindCainfo = moose.Annotator(CaM_Ca2_bindCa.path+'/info')

CaM_Ca3 = moose.Pool('/model/kinetics/CaM_g/CaM_Ca3')
CaM_Ca3info = moose.Annotator(CaM_Ca3.path+'/info')

CaM_Ca3_bindCa = moose.Reac('/model/kinetics/CaM_g/CaM_Ca3_bindCa')
CaM_Ca3_bindCainfo = moose.Annotator(CaM_Ca3_bindCa.path+'/info')

CaM_Ca4 = moose.Pool('/model/kinetics/CaM_g/CaM_Ca4')
CaM_Ca4info = moose.Annotator(CaM_Ca4.path+'/info')

#CaM_g connections

moose.connect('/model/kinetics/CaM_g/CaM_bindCa','sub','/model/kinetics/Ca_g/Ca','reac')
moose.connect('/model/kinetics/CaM_g/CaM_bindCa','sub','/model/kinetics/CaM_g/CaM','reac')
moose.connect('/model/kinetics/CaM_g/CaM_bindCa','prd','/model/kinetics/CaM_g/CaM_Ca','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca_bindCa','sub','/model/kinetics/Ca_g/Ca','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca_bindCa','sub','/model/kinetics/CaM_g/CaM_Ca','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca_bindCa','prd','/model/kinetics/CaM_g/CaM_Ca2','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca2_bindCa','sub','/model/kinetics/Ca_g/Ca','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca2_bindCa','sub','/model/kinetics/CaM_g/CaM_Ca2','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca2_bindCa','prd','/model/kinetics/CaM_g/CaM_Ca3','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca3_bindCa','sub','/model/kinetics/Ca_g/Ca','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca3_bindCa','sub','/model/kinetics/CaM_g/CaM_Ca3','reac')
moose.connect('/model/kinetics/CaM_g/CaM_Ca3_bindCa','prd','/model/kinetics/CaM_g/CaM_Ca4','reac')

#CaM_g parameters

moose.element('/model/kinetics/CaM_g/CaM').concInit = 20.0
moose.element('/model/kinetics/CaM_g/CaM_Ca').concInit = 0.0
moose.element('/model/kinetics/CaM_g/CaM_Ca2').concInit = 0.0
moose.element('/model/kinetics/CaM_g/CaM_Ca3').concInit = 0.0
moose.element('/model/kinetics/CaM_g/CaM_Ca4').concInit = 0.0
moose.element('/model/kinetics/CaM_g/CaM_bindCa').Kf = 8484.75
moose.element('/model/kinetics/CaM_g/CaM_bindCa').Kb = 8.4853
moose.element('/model/kinetics/CaM_g/CaM_Ca_bindCa').Kf = 8484.75
moose.element('/model/kinetics/CaM_g/CaM_Ca_bindCa').Kb = 8.4853
moose.element('/model/kinetics/CaM_g/CaM_Ca2_bindCa').Kf = 3600.022
moose.element('/model/kinetics/CaM_g/CaM_Ca2_bindCa').Kb = 10.0
moose.element('/model/kinetics/CaM_g/CaM_Ca3_bindCa').Kf = 465.002
moose.element('/model/kinetics/CaM_g/CaM_Ca3_bindCa').Kb = 10.0

#CaMKII_g molecules

CaMKII = moose.Pool('/model/kinetics/CaMKII_g/CaMKII')
CaMKIIinfo = moose.Annotator(CaMKII.path+'/info')

CaMKII_CaM = moose.Pool('/model/kinetics/CaMKII_g/CaMKII_CaM')
CaMKII_CaMinfo = moose.Annotator(CaMKII_CaM.path+'/info')

CaM_totCaMKII = moose.Reac('/model/kinetics/CaMKII_g/CaM_totCaMKII')
CaM_totCaMKIIinfo = moose.Annotator(CaM_totCaMKII.path+'/info')

CaMKII_thr286 = moose.Pool('/model/kinetics/CaMKII_g/CaMKII_thr286')
CaMKII_thr286info = moose.Annotator(CaMKII_thr286.path+'/info')

CaMKII_p_p_p = moose.Pool('/model/kinetics/CaMKII_g/CaMKII_p_p_p')
CaMKII_p_p_pinfo = moose.Annotator(CaMKII_p_p_p.path+'/info')

auto_CaMKII_p3 = moose.Reac('/model/kinetics/CaMKII_g/auto_CaMKII_p3')
auto_CaMKII_p3info = moose.Annotator(auto_CaMKII_p3.path+'/info')

tot_CaMKII_CaMpar = moose.Pool('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar')
tot_CaMKII_CaMparinfo = moose.Annotator(tot_CaMKII_CaMpar.path+'/info')

tot_CaMKII_CaM_p = moose.Enz('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p')
tot_CaMKII_CaM_pinfo = moose.Annotator(tot_CaMKII_CaM_p.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p', 'enz', '/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar', 'reac')

cplx1 = moose.Pool('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p/cplx1')
cplx1info = moose.Annotator(cplx1.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p','cplx','/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p/cplx1','reac')

tot_CaMKII_CaM_p_p_p = moose.Enz('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p')
tot_CaMKII_CaM_p_p_pinfo = moose.Annotator(tot_CaMKII_CaM_p_p_p.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p', 'enz', '/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar', 'reac')

cplx2 = moose.Pool('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p/cplx2')
cplx2info = moose.Annotator(cplx2.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p','cplx','/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p/cplx2','reac')

tot_auto_CaMKIIpar = moose.Pool('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar')
tot_auto_CaMKIIparinfo = moose.Annotator(tot_auto_CaMKIIpar.path+'/info')

tot_auto_CaMKII_p = moose.Enz('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p')
tot_auto_CaMKII_pinfo = moose.Annotator(tot_auto_CaMKII_p.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p', 'enz', '/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar', 'reac')

cplx9 = moose.Pool('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p/cplx9')
cplx9info = moose.Annotator(cplx9.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p','cplx','/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p/cplx9','reac')

tot_auto_CaMKII_p_p_p = moose.Enz('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p')
tot_auto_CaMKII_p_p_pinfo = moose.Annotator(tot_auto_CaMKII_p_p_p.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p', 'enz', '/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar', 'reac')

cplx10 = moose.Pool('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p/cplx10')
cplx10info = moose.Annotator(cplx10.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p','cplx','/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p/cplx10','reac')

CaMKII_thr286_p_CaMpar = moose.Pool('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar')
CaMKII_thr286_p_CaMparinfo = moose.Annotator(CaMKII_thr286_p_CaMpar.path+'/info')

CaMKII_thr286_p_CaM = moose.Enz('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM')
CaMKII_thr286_p_CaMinfo = moose.Annotator(CaMKII_thr286_p_CaM.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM', 'enz', '/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar', 'reac')

cplx14 = moose.Pool('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM/cplx14')
cplx14info = moose.Annotator(cplx14.path+'/info')

moose.connect('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM','cplx','/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM/cplx14','reac')

CaMCa4_bindCaMKII= moose.Reac('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKII')
CaMCa4_bindCaMKIIinfo = moose.Annotator(CaMCa4_bindCaMKII.path+'/info')

CaMKII_to_thr286 = moose.Reac('/model/kinetics/CaMKII_g/CaMKII_to_thr286')
CaMKII_to_thr286info = moose.Annotator(CaMKII_to_thr286.path+'/info')

CaMCa4_bindCaMKIIthr286 = moose.Reac('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKIIthr286')
CaMCa4_bindCaMKIIthr286info = moose.Annotator(CaMCa4_bindCaMKIIthr286.path+'/info')

#CaMKII_g connections

moose.connect('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKII','sub','/model/kinetics/CaM_g/CaM_Ca4','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKII','sub','/model/kinetics/CaMKII_g/CaMKII','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKII','prd','/model/kinetics/CaMKII_g/CaMKII_CaM','reac')
moose.connect('/model/kinetics/CaMKII_g/CaM_totCaMKII','sub','/model/kinetics/CaMKII_g/CaMKII_CaM','reac')
moose.connect('/model/kinetics/CaMKII_g/CaM_totCaMKII','prd','/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p','sub','/model/kinetics/CaMKII_g/CaMKII_CaM','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p','prd','/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMKII_to_thr286','sub','/model/kinetics/CaMKII_g/CaMKII','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMKII_to_thr286','sub','/model/kinetics/CaM_g/CaM_Ca4','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMKII_to_thr286','prd','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p','sub','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p','prd','/model/kinetics/CaMKII_g/CaMKII_p_p_p','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKIIthr286','sub','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKIIthr286','sub','/model/kinetics/CaM_g/CaM_Ca4','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKIIthr286','prd','/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar','reac')
moose.connect('/model/kinetics/CaMKII_g/auto_CaMKII_p3','sub','/model/kinetics/CaMKII_g/CaMKII_p_p_p','reac')
moose.connect('/model/kinetics/CaMKII_g/auto_CaMKII_p3','sub','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/CaMKII_g/auto_CaMKII_p3','prd','/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p','sub','/model/kinetics/CaMKII_g/CaMKII_CaM','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p','prd','/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p','sub','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p','prd','/model/kinetics/CaMKII_g/CaMKII_p_p_p','reac')

#CaMKII_g parameters

moose.element('/model/kinetics/CaMKII_g/CaMKII').concInit = 70.0
moose.element('/model/kinetics/CaMKII_g/CaMKII_CaM').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/CaMKII_thr286').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/CaMKII_p_p_p').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p/cplx1').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p/cplx2').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p').Km = 0.12229
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p').kcat = 0.5
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p').Km = 0.12228
moose.element('/model/kinetics/CaMKII_g/tot_CaMKII_CaMpar/tot_CaMKII_CaM_p_p_p').kcat = 6.0
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p/cplx10').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p/cplx9').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p').Km = 0.18838
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p_p_p').kcat = 6.0
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p').Km = 0.18837
moose.element('/model/kinetics/CaMKII_g/tot_auto_CaMKIIpar/tot_auto_CaMKII_p').kcat = 0.5
moose.element('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM/cplx14').concInit = 0.0
moose.element('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM').Km = 0.551
moose.element('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM').kcat = 0.3228
moose.element('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKII').Kf = 49999.85
moose.element('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKII').Kb = 5.0
moose.element('/model/kinetics/CaMKII_g/CaMKII_to_thr286').Kf = 0.02
moose.element('/model/kinetics/CaMKII_g/CaMKII_to_thr286').Kb = 0.02
moose.element('/model/kinetics/CaMKII_g/CaM_totCaMKII').Kf = 0.3353
moose.element('/model/kinetics/CaMKII_g/CaM_totCaMKII').Kb = 0.318
moose.element('/model/kinetics/CaMKII_g/auto_CaMKII_p3').Kf = 0.3515
moose.element('/model/kinetics/CaMKII_g/auto_CaMKII_p3').Kb = 0.3378
moose.element('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKIIthr286').Kf = 1000186.6
moose.element('/model/kinetics/CaMKII_g/CaMCa4_bindCaMKIIthr286').Kb = 0.1

#NO_g molecules

NOSp = moose.Pool('/model/kinetics/NO_g/NOSp')
NOSpinfo = moose.Annotator(NOSp.path+'/info')

LAr = moose.Pool('/model/kinetics/NO_g/LAr')
LArinfo = moose.Annotator(LAr.path+'/info')

anNOS_par = moose.Pool('/model/kinetics/NO_g/anNOS_par')
anNOS_parinfo = moose.Annotator(anNOS_par.path+'/info')

anNOS_LAr = moose.Enz('/model/kinetics/NO_g/anNOS_par/anNOS_LAr')
anNOS_LArinfo = moose.Annotator(anNOS_LAr.path+'/info')

moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LAr', 'enz', '/model/kinetics/NO_g/anNOS_par', 'reac')

cplx15 = moose.Pool('/model/kinetics/NO_g/anNOS_par/anNOS_LAr/cplx15')
cplx15info = moose.Annotator(cplx15.path+'/info')

moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LAr','cplx','/model/kinetics/NO_g/anNOS_par/anNOS_LAr/cplx15','reac')

anNOS_LCit = moose.Enz('/model/kinetics/NO_g/anNOS_par/anNOS_LCit')
anNOS_LCitinfo = moose.Annotator(anNOS_LCit.path+'/info')

moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LCit', 'enz', '/model/kinetics/NO_g/anNOS_par', 'reac')

cplx16 = moose.Pool('/model/kinetics/NO_g/anNOS_par/anNOS_LCit/cplx16')
cplx16info = moose.Annotator(cplx16.path+'/info')

moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LCit','cplx','/model/kinetics/NO_g/anNOS_par/anNOS_LCit/cplx16','reac')

NOH_LAr = moose.Pool('/model/kinetics/NO_g/NOH_LAr')
NOH_LArinfo = moose.Annotator(NOH_LAr.path+'/info')

NO = moose.Pool('/model/kinetics/NO_g/NO')
NOinfo = moose.Annotator(NO.path+'/info')

#NO_g connections

moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LAr','sub','/model/kinetics/NO_g/LAr','reac')
moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LAr','prd','/model/kinetics/NO_g/NOH_LAr','reac')
moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LCit','sub','/model/kinetics/NO_g/NOH_LAr','reac')
moose.connect('/model/kinetics/NO_g/anNOS_par/anNOS_LCit','prd','/model/kinetics/NO_g/NO','reac')

#NO_g parameters

moose.element('/model/kinetics/NO_g/NOSp').concInit = 0.5
moose.element('/model/kinetics/NO_g/LAr').concInit = 100.0
moose.element('/model/kinetics/NO_g/anNOS_par').concInit = 0.0
moose.element('/model/kinetics/NO_g/anNOS_par/anNOS_LAr/cplx15').concInit = 0.0
moose.element('/model/kinetics/NO_g/anNOS_par/anNOS_LAr').Km = 0.01
moose.element('/model/kinetics/NO_g/anNOS_par/anNOS_LAr').kcat = 16.0
moose.element('/model/kinetics/NO_g/anNOS_par/anNOS_LCit/cplx16').concInit = 0.0
moose.element('/model/kinetics/NO_g/anNOS_par/anNOS_LCit').Km = 0.01
moose.element('/model/kinetics/NO_g/anNOS_par/anNOS_LCit').kcat = 16.0
moose.element('/model/kinetics/NO_g/NOH_LAr').concInit = 0.0
moose.element('/model/kinetics/NO_g/NO').concInit = 0.0

#PP1_g molecules

PP1_I1 = moose.Pool('/model/kinetics/PP1_g/PP1_I1')
PP1_I1info = moose.Annotator(PP1_I1.path+'/info')

PP1_I1_active = moose.Reac('/model/kinetics/PP1_g/PP1_I1_active')
PP1_I1_activeinfo = moose.Annotator(PP1_I1_active.path+'/info')

PP1_active_par = moose.Pool('/model/kinetics/PP1_g/PP1_active_par')
PP1_active_parinfo = moose.Annotator(PP1_active_par.path+'/info')

PP1_active_CaMKIIthr286 = moose.Enz('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286')
PP1_active_CaMKIIthr286info = moose.Annotator(PP1_active_CaMKIIthr286.path+'/info')

moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286', 'enz', '/model/kinetics/PP1_g/PP1_active_par', 'reac')

cplx11 = moose.Pool('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286/cplx11')
cplx11info = moose.Annotator(cplx11.path+'/info')

moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286','cplx','/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286/cplx11','reac')

PP1_active_CaMKII_p_p_p = moose.Enz('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p')
PP1_active_CaMKII_p_p_pinfo = moose.Annotator(PP1_active_CaMKII_p_p_p.path+'/info')

moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p', 'enz', '/model/kinetics/PP1_g/PP1_active_par', 'reac')

cplx12 = moose.Pool('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p/cplx12')
cplx12info = moose.Annotator(cplx12.path+'/info')

moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p','cplx','/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p/cplx12','reac')

PP1_active_CaMKII_thr286_p_CaM = moose.Enz('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM')
PP1_active_CaMKII_thr286_p_CaMinfo = moose.Annotator(PP1_active_CaMKII_thr286_p_CaM.path+'/info')

moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM', 'enz', '/model/kinetics/PP1_g/PP1_active_par', 'reac')

cplx13 = moose.Pool('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM/cplx13')
cplx13info = moose.Annotator(cplx13.path+'/info')

moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM','cplx','/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM/cplx13','reac')

#PP1_g connections

moose.connect('/model/kinetics/PP1_g/PP1_I1_active','sub','/model/kinetics/PP1_g/PP1_I1','reac')
moose.connect('/model/kinetics/PP1_g/PP1_I1_active','prd','/model/kinetics/PP1_g/PP1_active_par','reac')
moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286','sub','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286','prd','/model/kinetics/CaMKII_g/CaMKII','reac')
moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p','sub','/model/kinetics/CaMKII_g/CaMKII_p_p_p','reac')
moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p','prd','/model/kinetics/CaMKII_g/CaMKII_thr286','reac')
moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM','sub','/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar','reac')
moose.connect('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM','prd','/model/kinetics/CaMKII_g/CaMKII_CaM','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM','sub','/model/kinetics/NO_g/NOSp','reac')
moose.connect('/model/kinetics/CaMKII_g/CaMKII_thr286_p_CaMpar/CaMKII_thr286_p_CaM','prd','/model/kinetics/NO_g/anNOS_par','reac')

#PP1_g parameters

moose.element('/model/kinetics/PP1_g/PP1_I1').concInit = 0.0
moose.element('/model/kinetics/PP1_g/PP1_active_par').concInit = 0.0018
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286/cplx11').concInit = 0.0
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286').Km = 0.00549
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKIIthr286').kcat = 0.35
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p/cplx12').concInit = 0.0
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p').Km = 0.005490
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_p_p_p').kcat = 0.35
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM/cplx13').concInit = 0.0
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM').Km = 0.00549
moose.element('/model/kinetics/PP1_g/PP1_active_par/PP1_active_CaMKII_thr286_p_CaM').kcat = 0.35
moose.element('/model/kinetics/PP1_g/PP1_I1_active').Kf = 1.0

#HN_g molecules

sGCfast = moose.Pool('/model/kinetics/HN_g/sGCfast')
sGCfastinfo = moose.Annotator(sGCfast.path+'/info')

sGCslow = moose.Pool('/model/kinetics/HN_g/sGCslow')
sGCslowinfo = moose.Annotator(sGCslow.path+'/info')

NO_sGCfast = moose.Pool('/model/kinetics/HN_g/NO_sGCfast')
NO_sGCfastinfo = moose.Annotator(NO_sGCfast.path+'/info')

NO_sGCslow = moose.Pool('/model/kinetics/HN_g/NO_sGCslow')
NO_sGCslowinfo = moose.Annotator(NO_sGCslow.path+'/info')

NO_sGC6coord = moose.Pool('/model/kinetics/HN_g/NO_sGC6coord')
NO_sGC6coordinfo = moose.Annotator(NO_sGC6coord.path+'/info')

NO_bindsGC_fast = moose.Reac('/model/kinetics/HN_g/NO_bindsGC_fast')
NO_bindsGC_fastinfo = moose.Annotator(NO_bindsGC_fast.path+'/info')

NO_bindsGC_slow = moose.Reac('/model/kinetics/HN_g/NO_bindsGC_slow')
NO_bindsGC_slowinfo = moose.Annotator(NO_bindsGC_slow.path+'/info')

act_sGC_fast = moose.Reac('/model/kinetics/HN_g/act_sGC_fast')
act_sGC_fastinfo = moose.Annotator(act_sGC_fast.path+'/info')

act_sGC_slow = moose.Reac('/model/kinetics/HN_g/act_sGC_slow')
act_sGC_slowinfo = moose.Annotator(act_sGC_slow.path+'/info')

form_6coord = moose.Reac('/model/kinetics/HN_g/form_6coord')
form_6coordinfo = moose.Annotator(form_6coord.path+'/info')

NO_GCpar = moose.Pool('/model/kinetics/HN_g/NO_GCpar')
NO_GCparinfo = moose.Annotator(NO_GCpar.path+'/info')

NO_GC = moose.Enz('/model/kinetics/HN_g/NO_GCpar/NO_GC')
NO_GCinfo = moose.Annotator(NO_GC.path+'/info')

moose.connect('/model/kinetics/HN_g/NO_GCpar/NO_GC', 'enz', '/model/kinetics/HN_g/NO_GCpar', 'reac')

cplx3 = moose.Pool('/model/kinetics/HN_g/NO_GCpar/NO_GC/cplx3')
cplx3info = moose.Annotator(cplx3.path+'/info')

moose.connect('/model/kinetics/HN_g/NO_GCpar/NO_GC','cplx','/model/kinetics/HN_g/NO_GCpar/NO_GC/cplx3','reac')

GTP = moose.Pool('/model/kinetics/HN_g/GTP')
GTPinfo = moose.Annotator(GTP.path+'/info')

cGMP = moose.Pool('/model/kinetics/HN_g/cGMP')
cGMPinfo = moose.Annotator(cGMP.path+'/info')

cGMP_bindPKG = moose.Reac('/model/kinetics/HN_g/cGMP_bindPKG')
cGMP_bindPKGinfo = moose.Annotator(cGMP_bindPKG.path+'/info')

PKG = moose.Pool('/model/kinetics/HN_g/PKG')
PKGinfo = moose.Annotator(PKG.path+'/info')

cGMP_PKG = moose.Pool('/model/kinetics/HN_g/cGMP_PKG')
cGMP_PKGinfo = moose.Annotator(cGMP_PKG.path+'/info')

cGMP2_form = moose.Reac('/model/kinetics/HN_g/cGMP2_form')
cGMP2_forminfo = moose.Annotator(cGMP2_form.path+'/info')

cGMP_PDEform = moose.Reac('/model/kinetics/HN_g/cGMP_PDEform')
cGMP_PDEforminfo = moose.Annotator(cGMP_PDEform.path+'/info')

cGMP2_PKGpar = moose.Pool('/model/kinetics/HN_g/cGMP2_PKGpar')
cGMP2_PKGparinfo = moose.Annotator(cGMP2_PKGpar.path+'/info')

cGMP_PKG_CREB = moose.Enz('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB')
cGMP_PKG_CREBainfo = moose.Annotator(cGMP_PKG_CREB.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB', 'enz', '/model/kinetics/HN_g/cGMP2_PKGpar', 'reac')

cplx4 = moose.Pool('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB/cplx4')
cplx4info = moose.Annotator(cplx4.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB','cplx','/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB/cplx4','reac')

cGMP_PKG_PDE = moose.Enz('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE')
cGMP_PKG_PDEainfo = moose.Annotator(cGMP_PKG_PDE.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE', 'enz', '/model/kinetics/HN_g/cGMP2_PKGpar', 'reac')

cplx17 = moose.Pool('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE/cplx17')
cplx17info = moose.Annotator(cplx17.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE','cplx','/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE/cplx17','reac')

CREB = moose.Pool('/model/kinetics/HN_g/CREB')
CREBinfo = moose.Annotator(CREB.path+'/info')

pCREB = moose.Pool('/model/kinetics/HN_g/pCREB')
pCREBinfo = moose.Annotator(pCREB.path+'/info')

cGMP_PDEpar = moose.Pool('/model/kinetics/HN_g/cGMP_PDEpar')
cGMP_PDEparinfo = moose.Annotator(cGMP_PDEpar.path+'/info')

cGMP_PDE = moose.Enz('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE')
cGMP_PDEainfo = moose.Annotator(cGMP_PDE.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE', 'enz', '/model/kinetics/HN_g/cGMP_PDEpar', 'reac')

cplx18 = moose.Pool('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE/cplx18')
cplx18info = moose.Annotator(cplx18.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE','cplx','/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE/cplx18','reac')

Myo_phosphatase_par = moose.Pool('/model/kinetics/HN_g/Myo_phosphatase_par')
Myo_phosphatase_parinfo = moose.Annotator(Myo_phosphatase_par.path+'/info')

Myo_phosphatase = moose.Enz('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase')
Myo_phosphataseinfo = moose.Annotator(Myo_phosphatase.path+'/info')

moose.connect('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase', 'enz', '/model/kinetics/HN_g/Myo_phosphatase_par', 'reac')

cplx19 = moose.Pool('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase/cplx19')
cplx19info = moose.Annotator(cplx19.path+'/info')

moose.connect('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase','cplx','/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase/cplx19','reac')

cGMP_PDE_p_par = moose.Pool('/model/kinetics/HN_g/cGMP_PDE_p_par')
cGMP_PDE_p_parinfo = moose.Annotator(cGMP_PDE_p_par.path+'/info')

cGMP_PDE_p = moose.Enz('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p')
cGMP_PDE_pinfo = moose.Annotator(cGMP_PDE_p.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p', 'enz', '/model/kinetics/HN_g/cGMP_PDE_p_par', 'reac')

cplx20 = moose.Pool('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p/cplx20')
cplx20info = moose.Annotator(cplx20.path+'/info')

moose.connect('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p','cplx','/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p/cplx20','reac')

PDE_par = moose.Pool('/model/kinetics/HN_g/PDE_par')
PDE_parinfo = moose.Annotator(PDE_par.path+'/info')

PDE = moose.Enz('/model/kinetics/HN_g/PDE_par/PDE')
PDEinfo = moose.Annotator(PDE.path+'/info')

moose.connect('/model/kinetics/HN_g/PDE_par/PDE', 'enz', '/model/kinetics/HN_g/PDE_par', 'reac')

cplx21 = moose.Pool('/model/kinetics/HN_g/PDE_par/PDE/cplx21')
cplx21info = moose.Annotator(cplx21.path+'/info')

moose.connect('/model/kinetics/HN_g/PDE_par/PDE','cplx','/model/kinetics/HN_g/PDE_par/PDE/cplx21','reac')

prime5_GMP = moose.Pool('/model/kinetics/HN_g/prime5_GMP')
prime5_GMPinfo = moose.Annotator(prime5_GMP.path+'/info')

#HN_g connections

moose.connect('/model/kinetics/HN_g/NO_bindsGC_fast','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/HN_g/NO_bindsGC_fast','sub','/model/kinetics/HN_g/sGCfast','reac')
moose.connect('/model/kinetics/HN_g/NO_bindsGC_fast','prd','/model/kinetics/HN_g/NO_sGCfast','reac')
moose.connect('/model/kinetics/HN_g/NO_bindsGC_slow','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/HN_g/NO_bindsGC_slow','sub','/model/kinetics/HN_g/sGCslow','reac')
moose.connect('/model/kinetics/HN_g/NO_bindsGC_slow','prd','/model/kinetics/HN_g/NO_sGCslow','reac')
moose.connect('/model/kinetics/HN_g/form_6coord','sub','/model/kinetics/HN_g/NO_sGCfast','reac')
moose.connect('/model/kinetics/HN_g/form_6coord','sub','/model/kinetics/HN_g/NO_sGCslow','reac')
moose.connect('/model/kinetics/HN_g/form_6coord','prd','/model/kinetics/HN_g/NO_sGC6coord','reac')
moose.connect('/model/kinetics/HN_g/act_sGC_fast','sub','/model/kinetics/HN_g/NO_sGC6coord','reac')
moose.connect('/model/kinetics/HN_g/act_sGC_slow','sub','/model/kinetics/HN_g/NO_sGC6coord','reac')
moose.connect('/model/kinetics/HN_g/act_sGC_fast','prd','/model/kinetics/HN_g/NO_GCpar','reac')
moose.connect('/model/kinetics/HN_g/act_sGC_slow','prd','/model/kinetics/HN_g/NO_GCpar','reac')
moose.connect('/model/kinetics/HN_g/NO_GCpar/NO_GC','sub','/model/kinetics/HN_g/GTP','reac')
moose.connect('/model/kinetics/HN_g/NO_GCpar/NO_GC','prd','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP_bindPKG','sub','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP_bindPKG','sub','/model/kinetics/HN_g/PKG','reac')
moose.connect('/model/kinetics/HN_g/cGMP_bindPKG','prd','/model/kinetics/HN_g/cGMP_PKG','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_form','sub','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_form','sub','/model/kinetics/HN_g/cGMP_PKG','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_form','prd','/model/kinetics/HN_g/cGMP2_PKGpar','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB','sub','/model/kinetics/HN_g/CREB','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB','prd','/model/kinetics/HN_g/pCREB','reac')
moose.connect('/model/kinetics/HN_g/cGMP_PDEform','sub','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP_PDEform','prd','/model/kinetics/HN_g/cGMP_PDEpar','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE','sub','/model/kinetics/HN_g/cGMP_PDEpar','reac')
moose.connect('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE','prd','/model/kinetics/HN_g/cGMP_PDE_p_par','reac')
moose.connect('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase','sub','/model/kinetics/HN_g/cGMP_PDE_p_par','reac')
moose.connect('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase','prd','/model/kinetics/HN_g/cGMP_PDEpar','reac')
moose.connect('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE','sub','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE','prd','/model/kinetics/HN_g/prime5_GMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p','sub','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p','prd','/model/kinetics/HN_g/prime5_GMP','reac')
moose.connect('/model/kinetics/HN_g/PDE_par/PDE','sub','/model/kinetics/HN_g/cGMP','reac')
moose.connect('/model/kinetics/HN_g/PDE_par/PDE','prd','/model/kinetics/HN_g/prime5_GMP','reac')

#HN_g parameters

moose.element('/model/kinetics/HN_g/sGCslow').concInit = 3.0
moose.element('/model/kinetics/HN_g/sGCfast').concInit = 3.0
moose.element('/model/kinetics/HN_g/NO_sGCslow').concInit = 0.0
moose.element('/model/kinetics/HN_g/NO_sGCfast').concInit = 0.0
moose.element('/model/kinetics/HN_g/NO_sGC6coord').concInit = 0.0
moose.element('/model/kinetics/HN_g/NO_bindsGC_fast').Kf = 700000.0
moose.element('/model/kinetics/HN_g/NO_bindsGC_fast').Kb = 800.0
moose.element('/model/kinetics/HN_g/NO_bindsGC_slow').Kf = 700000.0
moose.element('/model/kinetics/HN_g/NO_bindsGC_slow').Kb = 800.0
moose.element('/model/kinetics/HN_g/form_6coord').Kf = 850.0
moose.element('/model/kinetics/HN_g/act_sGC_fast').Kf = 20.0
moose.element('/model/kinetics/HN_g/act_sGC_fast').Kb = 0.2
moose.element('/model/kinetics/HN_g/act_sGC_slow').Kf = 5000.0
moose.element('/model/kinetics/HN_g/act_sGC_slow').Kb = 25.0
moose.element('/model/kinetics/HN_g/GTP').concInit = 9.99
moose.element('/model/kinetics/HN_g/NO_GCpar').concInit = 0.0
moose.element('/model/kinetics/HN_g/NO_GCpar/NO_GC/cplx3').concInit = 0.0
moose.element('/model/kinetics/HN_g/NO_GCpar/NO_GC').Km = 0.03
moose.element('/model/kinetics/HN_g/NO_GCpar/NO_GC').kcat = 22.05
moose.element('/model/kinetics/HN_g/cGMP').concInit = 0.0
moose.element('/model/kinetics/HN_g/PKG').concInit = 1.1
moose.element('/model/kinetics/HN_g/cGMP_bindPKG').Kf = 10000.0
moose.element('/model/kinetics/HN_g/cGMP_bindPKG').Kb = 81.0
moose.element('/model/kinetics/HN_g/cGMP_PKG').concInit = 0.0
moose.element('/model/kinetics/HN_g/PDE_par').concInit = 0.28
moose.element('/model/kinetics/HN_g/PDE_par/PDE').Km = 0.00098
moose.element('/model/kinetics/HN_g/PDE_par/PDE').kcat = 2.4
moose.element('/model/kinetics/HN_g/PDE_par/PDE/cplx21').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB/cplx4').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB').Km = 0.2691
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_CREB').kcat = 0.07932
moose.element('/model/kinetics/HN_g/CREB').concInit = 0.1
moose.element('/model/kinetics/HN_g/pCREB').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE').Km = 0.001004
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE').kcat = 0.6022
moose.element('/model/kinetics/HN_g/cGMP2_PKGpar/cGMP_PKG_PDE/cplx17').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP_PDE_p_par').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p').Km = 0.00058
moose.element('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p').kcat = 3.87
moose.element('/model/kinetics/HN_g/cGMP_PDE_p_par/cGMP_PDE_p/cplx20').concInit = 0.0
moose.element('/model/kinetics/HN_g/Myo_phosphatase_par').concInit = 0.5
moose.element('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase').Km = 0.01004
moose.element('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase').kcat = 1.98
moose.element('/model/kinetics/HN_g/Myo_phosphatase_par/Myo_phosphatase/cplx19').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP_PDEpar').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE').Km = 0.00098
moose.element('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE').kcat = 2.4
moose.element('/model/kinetics/HN_g/cGMP_PDEpar/cGMP_PDE/cplx18').concInit = 0.0
moose.element('/model/kinetics/HN_g/cGMP2_form').Kf = 10000.0
moose.element('/model/kinetics/HN_g/cGMP2_form').Kb = 37.0
moose.element('/model/kinetics/HN_g/cGMP_PDEform').Kf = 10.0
moose.element('/model/kinetics/HN_g/cGMP_PDEform').Kb = 13.0
moose.element('/model/kinetics/HN_g/prime5_GMP').concInit = 0.0

#DR_g molecules

radical_NO = moose.Reac('/model/kinetics/DR_g/radical_NO')
radical_NOinfo = moose.Annotator(radical_NO.path+'/info')

anion_NO = moose.Reac('/model/kinetics/DR_g/anion_NO')
anion_NOinfo = moose.Annotator(anion_NO.path+'/info')

NO_R = moose.Pool('/model/kinetics/DR_g/NO_R')
NO_Rinfo = moose.Annotator(NO_R.path+'/info')

NO_n = moose.Pool('/model/kinetics/DR_g/NO_n')
NO_ninfo = moose.Annotator(NO_n.path+'/info')

O2R = moose.Pool('/model/kinetics/DR_g/O2R')
O2Rinfo = moose.Annotator(O2R.path+'/info')

O2 = moose.Pool('/model/kinetics/DR_g/O2')
O2info = moose.Annotator(O2.path+'/info')

NO_RbindO2R = moose.Reac('/model/kinetics/DR_g/NO_RbindO2R')
NO_RbindO2Rinfo = moose.Annotator(NO_RbindO2R.path+'/info')

NO_nbindO2 = moose.Reac('/model/kinetics/DR_g/NO_nbindO2')
NO_nbindO2info = moose.Annotator(NO_nbindO2.path+'/info')

ONOOpar = moose.Pool('/model/kinetics/DR_g/ONOOpar')
ONOOparinfo = moose.Annotator(ONOOpar.path+'/info')

ONOO = moose.Enz('/model/kinetics/DR_g/ONOOpar/ONOO')
ONOOinfo = moose.Annotator(ONOO.path+'/info')

moose.connect( '/model/kinetics/DR_g/ONOOpar/ONOO', 'enz', '/model/kinetics/DR_g/ONOOpar', 'reac' )

cplx6 = moose.Pool('/model/kinetics/DR_g/ONOOpar/ONOO/cplx6')
cplx6info = moose.Annotator(cplx6.path+'/info')

moose.connect('/model/kinetics/DR_g/ONOOpar/ONOO','cplx','/model/kinetics/DR_g/ONOOpar/ONOO/cplx6','reac')

aPARP_par = moose.Pool('/model/kinetics/DR_g/aPARP_par')
aPARP_parinfo = moose.Annotator(aPARP_par.path+'/info')

aPARP_PARpol = moose.Enz('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol')
aPARP_PARpolinfo = moose.Annotator(aPARP_PARpol.path+'/info')

moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol', 'enz', '/model/kinetics/DR_g/aPARP_par', 'reac')

cplx7 = moose.Pool('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol/cplx7')
cplx7info = moose.Annotator(cplx7.path+'/info')

moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol','cplx','/model/kinetics/DR_g/aPARP_par/aPARP_PARpol/cplx7','reac')

aPARP_ADPpol = moose.Enz('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol')
aPARP_ADPpolinfo = moose.Annotator(aPARP_ADPpol.path+'/info')

moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol', 'enz', '/model/kinetics/DR_g/aPARP_par', 'reac')

cplx22 = moose.Pool('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol/cplx22')
cplx22info = moose.Annotator(cplx22.path+'/info')

moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol','cplx','/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol/cplx22','reac')

PARP = moose.Pool('/model/kinetics/DR_g/PARP')
PARPinfo = moose.Annotator(PARP.path+'/info')

PAR = moose.Pool('/model/kinetics/DR_g/PAR')
PARinfo = moose.Annotator(PAR.path+'/info')

PAR_pol_par = moose.Pool('/model/kinetics/DR_g/PAR_pol_par')
PAR_pol_parinfo = moose.Annotator(PAR_pol_par.path+'/info')

PAR_pol = moose.Enz('/model/kinetics/DR_g/PAR_pol_par/PAR_pol')
PAR_polinfo = moose.Annotator(PAR_pol.path+'/info')

moose.connect('/model/kinetics/DR_g/PAR_pol_par/PAR_pol', 'enz', '/model/kinetics/DR_g/PAR_pol_par', 'reac')

cplx8 = moose.Pool('/model/kinetics/DR_g/PAR_pol_par/PAR_pol/cplx8')
cplx8info = moose.Annotator(cplx8.path+'/info')

moose.connect('/model/kinetics/DR_g/PAR_pol_par/PAR_pol','cplx','/model/kinetics/DR_g/PAR_pol_par/PAR_pol/cplx8','reac')

AIF = moose.Pool('/model/kinetics/DR_g/AIF')
AIFinfo = moose.Annotator(AIF.path+'/info')

AIF_PAR = moose.Pool('/model/kinetics/DR_g/AIF_PAR')
AIF_PARinfo = moose.Annotator(AIF_PAR.path+'/info')

MIF = moose.Pool('/model/kinetics/DR_g/MIF')
MIFinfo = moose.Annotator(MIF.path+'/info')

MIF_AIF = moose.Pool('/model/kinetics/DR_g/MIF_AIF')
MIF_AIFinfo = moose.Annotator(MIF_AIF.path+'/info')

MIF_bindAIF = moose.Reac('/model/kinetics/DR_g/MIF_bindAIF')
MIF_bindAIFinfo = moose.Annotator(MIF_bindAIF.path+'/info')

NAD = moose.Pool('/model/kinetics/DR_g/NAD')
NADinfo = moose.Annotator(NAD.path+'/info')

Poly_ADP_Ribosy = moose.Pool('/model/kinetics/DR_g/Poly_ADP_Ribosy')
Poly_ADP_Ribosyinfo = moose.Annotator(Poly_ADP_Ribosy.path+'/info')

Nicotinamide = moose.Pool('/model/kinetics/DR_g/Nicotinamide')
Nicotinamideinfo = moose.Annotator(Nicotinamide.path+'/info')

Nicotinamide_form = moose.Reac('/model/kinetics/DR_g/Nicotinamide_form')
Nicotinamide_forminfo = moose.Annotator(Nicotinamide_form.path+'/info')

Nicotinamide_dis = moose.Reac('/model/kinetics/DR_g/Nicotinamide_dis')
Nicotinamide_disinfo = moose.Annotator(Nicotinamide_dis.path+'/info')

#DR_g connections

moose.connect('/model/kinetics/DR_g/radical_NO','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/DR_g/anion_NO','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/DR_g/radical_NO','prd','/model/kinetics/DR_g/NO_R','reac')
moose.connect('/model/kinetics/DR_g/anion_NO','prd','/model/kinetics/DR_g/NO_n','reac')
moose.connect('/model/kinetics/DR_g/NO_RbindO2R','sub','/model/kinetics/DR_g/NO_R','reac')
moose.connect('/model/kinetics/DR_g/NO_nbindO2','sub','/model/kinetics/DR_g/NO_n','reac')
moose.connect('/model/kinetics/DR_g/NO_RbindO2R','sub','/model/kinetics/DR_g/O2R','reac')
moose.connect('/model/kinetics/DR_g/NO_nbindO2','sub','/model/kinetics/DR_g/O2','reac')
moose.connect('/model/kinetics/DR_g/NO_RbindO2R','prd','/model/kinetics/DR_g/ONOOpar','reac')
moose.connect('/model/kinetics/DR_g/NO_nbindO2','prd','/model/kinetics/DR_g/ONOOpar','reac')
moose.connect('/model/kinetics/DR_g/ONOOpar/ONOO','sub','/model/kinetics/DR_g/PARP','reac')
moose.connect('/model/kinetics/DR_g/ONOOpar/ONOO','prd','/model/kinetics/DR_g/aPARP_par','reac')
moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol','sub','/model/kinetics/DR_g/PAR','reac')
moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol','prd','/model/kinetics/DR_g/PAR_pol_par','reac')
moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol','sub','/model/kinetics/DR_g/NAD','reac')
moose.connect('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol','prd','/model/kinetics/DR_g/Poly_ADP_Ribosy','reac')
moose.connect('/model/kinetics/DR_g/Nicotinamide_form','sub','/model/kinetics/DR_g/Poly_ADP_Ribosy','reac')
moose.connect('/model/kinetics/DR_g/Nicotinamide_form','prd','/model/kinetics/DR_g/Nicotinamide','reac')
moose.connect('/model/kinetics/DR_g/Nicotinamide_dis','sub','/model/kinetics/DR_g/Nicotinamide','reac')
moose.connect('/model/kinetics/DR_g/Nicotinamide_dis','prd','/model/kinetics/DR_g/NAD','reac')
moose.connect('/model/kinetics/DR_g/PAR_pol_par/PAR_pol','sub','/model/kinetics/DR_g/AIF','reac')
moose.connect('/model/kinetics/DR_g/PAR_pol_par/PAR_pol','prd','/model/kinetics/DR_g/AIF_PAR','reac')
moose.connect('/model/kinetics/DR_g/MIF_bindAIF','sub','/model/kinetics/DR_g/AIF_PAR','reac')
moose.connect('/model/kinetics/DR_g/MIF_bindAIF','sub','/model/kinetics/DR_g/MIF','reac')
moose.connect('/model/kinetics/DR_g/MIF_bindAIF','prd','/model/kinetics/DR_g/MIF_AIF','reac')

#DR_g parameters

moose.element('/model/kinetics/DR_g/NO_R').concInit = 0.0
moose.element('/model/kinetics/DR_g/O2R').concInit = 0.5
moose.element('/model/kinetics/DR_g/NO_n').concInit = 0.0
moose.element('/model/kinetics/DR_g/O2').concInit = 0.5
moose.element('/model/kinetics/DR_g/radical_NO').Kf = 2.0
moose.element('/model/kinetics/DR_g/radical_NO').Kb = 2.0
moose.element('/model/kinetics/DR_g/anion_NO').Kf = 2.0
moose.element('/model/kinetics/DR_g/anion_NO').Kb = 2.0
moose.element('/model/kinetics/DR_g/NO_RbindO2R').Kf = 2.0
moose.element('/model/kinetics/DR_g/NO_RbindO2R').Kb = 2.0
moose.element('/model/kinetics/DR_g/NO_nbindO2').Kf = 2.0
moose.element('/model/kinetics/DR_g/NO_nbindO2').Kb = 2.0
moose.element('/model/kinetics/DR_g/ONOOpar').concInit = 0.0
moose.element('/model/kinetics/DR_g/ONOOpar/ONOO').Km = 2.0
moose.element('/model/kinetics/DR_g/ONOOpar/ONOO').kcat = 2.0
moose.element('/model/kinetics/DR_g/ONOOpar/ONOO/cplx6').concInit = 0.0
moose.element('/model/kinetics/DR_g/PARP').concInit = 20.0
moose.element('/model/kinetics/DR_g/aPARP_par').concInit = 0.0
moose.element('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol').Km = 2.0
moose.element('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol').kcat = 2.0
moose.element('/model/kinetics/DR_g/aPARP_par/aPARP_PARpol/cplx7').concInit = 0.0
moose.element('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol').Km = 2.0
moose.element('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol').kcat = 2.0
moose.element('/model/kinetics/DR_g/aPARP_par/aPARP_ADPpol/cplx22').concInit = 0.0
moose.element('/model/kinetics/DR_g/Poly_ADP_Ribosy').concInit = 0.0
moose.element('/model/kinetics/DR_g/Nicotinamide').concInit = 0.0
moose.element('/model/kinetics/DR_g/NAD').concInit = 0.0
moose.element('/model/kinetics/DR_g/Nicotinamide_form').Kf = 2.0
moose.element('/model/kinetics/DR_g/Nicotinamide_form').Kb = 2.0
moose.element('/model/kinetics/DR_g/Nicotinamide_dis').Kf = 2.0
moose.element('/model/kinetics/DR_g/Nicotinamide_dis').Kb = 2.0
moose.element('/model/kinetics/DR_g/PAR').concInit = 0.1
moose.element('/model/kinetics/DR_g/PAR_pol_par').concInit = 0.0
moose.element('/model/kinetics/DR_g/PAR_pol_par/PAR_pol').Km = 2.0
moose.element('/model/kinetics/DR_g/PAR_pol_par/PAR_pol').kcat = 2.0
moose.element('/model/kinetics/DR_g/PAR_pol_par/PAR_pol/cplx8').concInit = 0.0
moose.element('/model/kinetics/DR_g/AIF').concInit = 0.5
moose.element('/model/kinetics/DR_g/AIF_PAR').concInit = 0.0
moose.element('/model/kinetics/DR_g/MIF').concInit = 0.5
moose.element('/model/kinetics/DR_g/MIF_bindAIF').Kf = 2.0
moose.element('/model/kinetics/DR_g/MIF_bindAIF').Kb = 2.0
moose.element('/model/kinetics/DR_g/MIF_AIF').concInit = 0.0

#Ap_g molecules

GAPDH = moose.Pool('/model/kinetics/Ap_g/GAPDH')
GAPDHinfo = moose.Annotator(GAPDH.path+'/info')

GOSPEL = moose.Pool('/model/kinetics/Ap_g/GOSPEL')
GOSPELinfo = moose.Annotator(GOSPEL.path+'/info')

NO_bindGAPDH = moose.Reac('/model/kinetics/Ap_g/NO_bindGAPDH')
NO_bindGAPDHinfo = moose.Annotator(NO_bindGAPDH.path+'/info')

NO_bindGOSPEL = moose.Reac('/model/kinetics/Ap_g/NO_bindGOSPEL')
NO_bindGOSPEL = moose.Annotator(NO_bindGOSPEL.path+'/info')

SNOGAPDH = moose.Pool('/model/kinetics/Ap_g/SNOGAPDH')
SNOGAPDHinfo = moose.Annotator(SNOGAPDH.path+'/info')

SNOGOSPEL = moose.Pool('/model/kinetics/Ap_g/SNOGOSPEL')
SNOGOSPELinfo = moose.Annotator(SNOGOSPEL.path+'/info')

Siah = moose.Pool('/model/kinetics/Ap_g/Siah')
Siahinfo = moose.Annotator(Siah.path+'/info')

Siah_bindSNOGAPDH = moose.Reac('/model/kinetics/Ap_g/Siah_bindSNOGAPDH')
Siah_bindSNOGAPDH = moose.Annotator(Siah_bindSNOGAPDH.path+'/info')

SNOGOSPEL_bindSNOGAPDH = moose.Reac('/model/kinetics/Ap_g/SNOGOSPEL_bindSNOGAPDH')
SNOGOSPEL_bindSNOGAPDH = moose.Annotator(SNOGOSPEL_bindSNOGAPDH.path+'/info')

SSG_par = moose.Pool('/model/kinetics/Ap_g/SSG_par')
SSG_parinfo = moose.Annotator(SSG_par.path+'/info')

SSG = moose.Enz('/model/kinetics/Ap_g/SSG_par/SSG')
SSGinfo = moose.Annotator(SSG.path+'/info')

moose.connect('/model/kinetics/Ap_g/SSG_par/SSG', 'enz', '/model/kinetics/Ap_g/SSG_par', 'reac')

cplx5 = moose.Pool('/model/kinetics/Ap_g/SSG_par/SSG/cplx5')
cplx5info = moose.Annotator(cplx5.path+'/info')

moose.connect('/model/kinetics/Ap_g/SSG_par/SSG','cplx','/model/kinetics/Ap_g/SSG_par/SSG/cplx5','reac')

SGG = moose.Pool('/model/kinetics/Ap_g/SGG')
SGGinfo = moose.Annotator(SGG.path+'/info')

HDAC2 = moose.Pool('/model/kinetics/Ap_g/HDAC2')
HDAC2info = moose.Annotator(HDAC2.path+'/info')

SSG_HDAC2 = moose.Pool('/model/kinetics/Ap_g/SSG_HDAC2')
SSG_HDAC2info = moose.Annotator(SSG_HDAC2.path+'/info')

SNOGOSPEL_inh_SSG = moose.Reac('/model/kinetics/Ap_g/SNOGOSPEL_inh_SSG')
SNOGOSPEL_inh_SSG = moose.Annotator(SNOGOSPEL_inh_SSG.path+'/info')

#Ap_g connections

moose.connect('/model/kinetics/Ap_g/NO_bindGAPDH','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGAPDH','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGAPDH','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGAPDH','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGOSPEL','sub','/model/kinetics/NO_g/NO','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGAPDH','sub','/model/kinetics/Ap_g/GAPDH','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGOSPEL','sub','/model/kinetics/Ap_g/GOSPEL','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGAPDH','prd','/model/kinetics/Ap_g/SNOGAPDH','reac')
moose.connect('/model/kinetics/Ap_g/NO_bindGOSPEL','prd','/model/kinetics/Ap_g/SNOGOSPEL','reac')
moose.connect('/model/kinetics/Ap_g/Siah_bindSNOGAPDH','sub','/model/kinetics/Ap_g/SNOGAPDH','reac')
moose.connect('/model/kinetics/Ap_g/Siah_bindSNOGAPDH','sub','/model/kinetics/Ap_g/Siah','reac')
moose.connect('/model/kinetics/Ap_g/Siah_bindSNOGAPDH','sub','/model/kinetics/Ap_g/Siah','reac')
moose.connect('/model/kinetics/Ap_g/Siah_bindSNOGAPDH','prd','/model/kinetics/Ap_g/SSG_par','reac')
moose.connect('/model/kinetics/Ap_g/SNOGOSPEL_bindSNOGAPDH','sub','/model/kinetics/Ap_g/SNOGAPDH','reac')
moose.connect('/model/kinetics/Ap_g/SNOGOSPEL_bindSNOGAPDH','sub','/model/kinetics/Ap_g/SNOGOSPEL','reac')
moose.connect('/model/kinetics/Ap_g/SNOGOSPEL_bindSNOGAPDH','prd','/model/kinetics/Ap_g/SGG','reac')
moose.connect('/model/kinetics/Ap_g/SSG_par/SSG','sub','/model/kinetics/Ap_g/HDAC2','reac')
moose.connect('/model/kinetics/Ap_g/SSG_par/SSG','prd','/model/kinetics/Ap_g/SSG_HDAC2','reac')
moose.connect('/model/kinetics/Ap_g/SNOGOSPEL_inh_SSG','sub','/model/kinetics/Ap_g/SNOGOSPEL','reac')
moose.connect('/model/kinetics/Ap_g/SNOGOSPEL_inh_SSG','prd','/model/kinetics/Ap_g/SSG_par','reac')

#Ap_g parameters

moose.element('/model/kinetics/Ap_g/GAPDH').concInit = 0.5
moose.element('/model/kinetics/Ap_g/GOSPEL').concInit = 0.01  
moose.element('/model/kinetics/Ap_g/Siah').concInit = 0.1
moose.element('/model/kinetics/Ap_g/HDAC2').concInit = 0.5
moose.element('/model/kinetics/Ap_g/NO_bindGAPDH').Kf = 0.8072
moose.element('/model/kinetics/Ap_g/NO_bindGAPDH').Kb = 0.4796
moose.element('/model/kinetics/Ap_g/NO_bindGOSPEL').Kf = 2.359
moose.element('/model/kinetics/Ap_g/NO_bindGOSPEL').Kb = 0.5176
moose.element('/model/kinetics/Ap_g/SNOGAPDH').concInit = 0.0
moose.element('/model/kinetics/Ap_g/SNOGOSPEL').concInit = 0.0
moose.element('/model/kinetics/Ap_g/Siah_bindSNOGAPDH').Kf = 1.003
moose.element('/model/kinetics/Ap_g/Siah_bindSNOGAPDH').Kb = 0.3546
moose.element('/model/kinetics/Ap_g/SNOGOSPEL_bindSNOGAPDH').Kf = 0.3669 
moose.element('/model/kinetics/Ap_g/SNOGOSPEL_bindSNOGAPDH').Kb = 0.9291 
moose.element('/model/kinetics/Ap_g/SNOGOSPEL_inh_SSG').Kf = 0.3425
moose.element('/model/kinetics/Ap_g/SNOGOSPEL_inh_SSG').Kb = 0.5017 
moose.element('/model/kinetics/Ap_g/SGG').concInit = 0.0
moose.element('/model/kinetics/Ap_g/SSG_par').concInit = 0.0
moose.element('/model/kinetics/Ap_g/SSG_par/SSG').Km = 0.6663
moose.element('/model/kinetics/Ap_g/SSG_par/SSG').kcat = 1.874
moose.element('/model/kinetics/Ap_g/SSG_par/SSG/cplx5').concInit = 0.0
moose.element('/model/kinetics/Ap_g/SSG_HDAC2').concInit = 0.0


moose.writeKkit('/model', 'NOS.g')
moose.writeSBML('/model', 'NOS.xml')

