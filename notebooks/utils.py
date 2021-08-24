

# The files we are going to be loading, along with necessary matching information
atlas_root_treename = 'mini'
files = {
    'data':
        {
            'files': [
                'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/Data/data_A.4lep.root',
                'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/Data/data_B.4lep.root',
                'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/Data/data_C.4lep.root',
                'root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/Data/data_D.4lep.root',
                ],
            'nickname': 'data',
            'treename': atlas_root_treename,
        },
    'ggH125_ZZ4lep':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root'],
            'nickname': 'ggH125_ZZ4lep',
            'treename': atlas_root_treename,
        },
    'ZH125_ZZ4lep':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_341947.ZH125_ZZ4lep.4lep.root'],
            'nickname': 'ZH125_ZZ4lep',
            'treename': atlas_root_treename,
        },
    'VBFH125_ZZ4lep':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_344235.VBFH125_ZZ4lep.4lep.root'],
            'nickname': 'VBFH125_ZZ4lep',
            'treename': atlas_root_treename,
        },
    'WH125_ZZ4lep':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_341964.WH125_ZZ4lep.4lep.root'],
            'nickname': 'WH125_ZZ4lep',
            'treename': atlas_root_treename,
        },
    'ZqqZll':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_363356.ZqqZll.4lep.root'],
            'nickname': 'ZqqZll',
            'treename': atlas_root_treename,
        },
    # A very weird bug occurs in this file! Awkward fails. No idea what causes this.
    # To repo, run everything, then uncomment this to watch.
    # 'WqqZll':
    #     {
    #         'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/2lep/MC/mc_363358.WqqZll.2lep.root'],
    #         'nickname': 'WqqZll',
    #         'treename': atlas_root_treename,
    #     },
    'WpqqWmlv':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/2lep/MC/mc_363359.WpqqWmlv.2lep.root'],
            'nickname': 'WpqqWmlv',
            'treename': atlas_root_treename,
        },
    'WplvWmqq':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/2lep/MC/mc_363360.WplvWmqq.2lep.root'],
            'nickname': 'WplvWmqq',
            'treename': atlas_root_treename,
        },
    'WlvZqq':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/2lep/MC/mc_363489.WlvZqq.2lep.root'],
            'nickname': 'WlvZqq',
            'treename': atlas_root_treename,
        },
    'llll':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_363490.llll.4lep.root'],
            'nickname': 'llll',
            'treename': atlas_root_treename,
        },
    'lllv':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_363491.lllv.4lep.root'],
            'nickname': 'lllv',
            'treename': atlas_root_treename,
        },
    'llvv':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_363492.llvv.4lep.root'],
            'nickname': 'llvv',
            'treename': atlas_root_treename,
        },
    'lvvv':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/2lep/MC/mc_363493.lvvv.2lep.root'],
            'nickname': 'lvvv',
            'treename': atlas_root_treename,
        },
    'Zee':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_361106.Zee.4lep.root'],
            'nickname': 'Zee',
            'treename': atlas_root_treename,
        },
    'Zmumu':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_361107.Zmumu.4lep.root'],
            'nickname': 'Zmumu',
            'treename': atlas_root_treename,
        },
    'Ztautau':
        {
            'files': ['root://eospublic.cern.ch//eos/opendata/atlas/OutreachDatasets/2020-01-22/4lep/MC/mc_361108.Ztautau.4lep.root'],
            'nickname': 'Ztautau',
            'treename': atlas_root_treename,
        },
}


cms_files = {
    'data_2e_7TeV':
        {
            'files': 'cernopendata://16',
            'nickname': 'data_2e_7TeV'
        },
    'data_2mu_7TeV':
        {
            'files': 'cernopendata://17',
            'nickname': 'data_2e_7TeV'
        },
    'data_2mu_8TeV_B':
        {
            'files': 'cernopendata://6004',
            'nickname': 'data_2mu_8TeV_B'
        },
    'data_2mu_8TeV_C':
        {
            'files': 'cernopendata://6030',
            'nickname': 'data_2mu_8TeV_C'
        },
    'data_2e_8TeV_B':
        {
            'files': 'cernopendata://6029',
            'nickname': 'data_2e_8TeV_B'
        },
    'data_2e_8TeV_C':
        {
            'files': 'cernopendata://6003',
            'nickname': 'data_2e_8TeV_C'
        },
    'SMHiggsToZZTo4L_M_125_7TeV':
        {
            'files': 'cernopendata://1507',
            'nickname': 'SMHiggsToZZTo4L_M_125_7TeV'
        },
    'SMHiggsToZZTo4L_M-125_8TeV':
        {
            'files': 'cernopendata://9356',
            'nickname': 'SMHiggsToZZTo4L_M-125_8TeV'
        },
    'ZZTo4mu_mll4_7TeV':
        {
            'files': 'cernopendata://1651',
            'nickname': 'ZZTo4mu_mll4_7TeV'
        },
    'ZZTo4e_mll4_7TeV_II':
        {
            'files': 'cernopendata://1648',
            'nickname': 'ZZTo4e_mll4_7TeV_II'
        },
    'ZZTo2e2mu_mll4_7TeV':
        {
            'files': 'cernopendata://1382',
            'nickname': 'ZZTo2e2mu_mll4_7TeV'
        },
    'DYJetsToLL_M-50_7TeV':
        {
            'files': 'cernopendata://1394',
            'nickname': 'DYJetsToLL_M_50_7TeV'
        },
    'DYJetsToLL_M-10To50_TuneZ2_7TeV':
        {
            'files': 'cernopendata://1393',
            'nickname': 'DYJ_M_10To50_7TeV'
        },
    'DYJetsToLL_M-50_TuneZ2Star_8TeV':
        {
            'files': 'cernopendata://7731',
            'nickname': 'DYJ_M50_8TeV'
        },
    'DYJetsToLL_M-10to50_HT-200to400_TuneZ2star_8TeV':
        {
            'files': 'cernopendata://7727',
            'nickname': 'DYJ_10to50_HT_200to400S_8TeV'
        },
    'DYJetsToLL_M-10to50_HT-400toInf_TuneZ2star_8TeV':
        {
            'files': 'cernopendata://7728',
            'nickname': 'DYJ_10to50_HT_400_8TeV'
        },
    'TTTo2L2Nu2B_7TeV':
        {
            'files': 'cernopendata://1360',
            'nickname': 'TTTo2L2Nu2B_7TeV'
        },
    'ZZTo4mu_8TeV':
        {
            'files': 'cernopendata://10071',
            'nickname': 'ZZTo4mu_8TeV'
        },
    'ZZTo4e_8TeV':
        {
            'files': 'cernopendata://10065',
            'nickname': 'ZZTo4e_8TeV'
        },
    'ZZTo2e2mu_8TeV':
        {
            'files': 'cernopendata://10054',
            'nickname': 'ZZTo2e2mu_8TeV'
        },
    'TTbar_8TeV':
        {
            'files': 'cernopendata://9518',
            'nickname': 'TTbar_8TeV'
        },
}
