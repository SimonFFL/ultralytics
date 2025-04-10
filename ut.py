import os

if __name__ == "__main__":
    names = ['liver_FPH', 'IVC_FPH', 'PV_FPH', 'liver_SPH', 'IVC_SPH',
       'LHV_SPH', 'MHV_SPH', 'RHV_SPH', 'ABAO_LL', 'DIAPH_LL', 'liver_LL',
       'liver_RL', 'IVC_RL', 'RHV_RL', 'PV_RL', 'DIAPH_RL', 'liver_LPV',
       'IS_LPV', 'GB_LAGB', 'liver_LAGB', 'GB_SAGB', 'liver_SAGB',
       'liver_LAEHBD', 'PV_LAEHBD', 'EHBD_LAEHBD', 'SP_LASP', 'SV_LASP',
       'IVC_LAPA', 'PA_LAPA', 'PV_LAPA', 'SV_LAPA', 'PA_SAPA', 'SMV_SAPA',
       'IVC_LAIVC', 'liver_LAIVC', 'DIAPH_LAIVC', 'PAV_SAPA', 'PAD_SAPA',
       'liver_FPH_LAEHBD', 'liver_RL_SPH_LPV', 'liver_LL_LAIVC',
       'PV_FPH_LAEHBD', 'DIAPH_LL_LAIVC', 'IVC_RL_SPH', 'RHV_RL_SPH']
    
    print("names:", names)

    for i, name in enumerate(names):
        print(f"{i}: {name}")