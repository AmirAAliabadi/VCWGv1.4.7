from UWG import UWG
from BEMMonthly import BEMMonthly
import numpy
import os

epw_filename = 'ERA5-Toronto-2020.epw'
initialization_name = 'initialize_Toronto'
case_name = 'Toronto-2020-PassiveHouse-NV'
Months = ['Jan.txt', 'Feb.txt', 'Mar.txt', 'Apr.txt', 'May.txt', 'Jun.txt', 'Jul.txt', 'Aug.txt', 'Sep.txt', 'Oct.txt', 'Nov.txt', 'Dec.txt']
OutputData = ['BEM', 'q_profiles', 'Tepw', 'TKE_profiles', 'Tr_profiles', 'Tu_profiles', 'U_profiles', 'V_profiles']

#Advanced energy heat mode for 12 months: Heating mode (1), cooling mode (0), no renewable energy (2), PV and Wind only (3)
Adv_ene_heat_mode = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

# Run for each month
for i in range(1,13,1):
    # Create the name of initialization file: e.g. initialize_Toronto_1.uwg
    param_filename = initialization_name+'_'+str(i)+'.uwg'
    uwg = UWG(epw_filename, param_filename, '', '', '', '')
    uwg.run()
    BEMMonthly(Adv_ene_heat_mode[i-1], 'Output/Perf-Metrics-'+case_name+'-'+Months[i-1])

    # Rename all hourly files
    for output_type in OutputData:
        input_file = "Output/{}_hourly.txt".format(output_type)
        output_file = "Output/{}_hourly-{}-{}".format(output_type, case_name, Months[i-1])
        os.rename(input_file, output_file)

