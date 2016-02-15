from datetime import date  # module nécessaire pour la définition des dates, dont notamment les dates de naissances
from openfisca_core import periods
import openfisca_france    # module décrivant le système socio-fiscal français
from openfisca_france.tests import base
#from modulation_allocations_familiales.reforms import af_modulation
from openfisca_core import rates
TaxBenefitSystem = openfisca_france.init_country()  # Initialisation de la classe décrivant le système socio-fiscal français
print TaxBenefitSystem
tax_benefit_system = TaxBenefitSystem()  # Création d'une instance du système socio-fiscal français
import cPickle
from openfisca_utils.make_ready_to_use_scenario import make_couple_with_child_scenario

salaire_de_base_min = 0
salaire_de_base_maximal = 2*10**5
count = 10000
year_range = range(2012,2016)
child_range = range (0, 5)
axes_variable = 'salaire_de_base'
simulation_var = ['rsa','af','salaire_net','rni','br_pf','aide_logement','decote_gain_fiscal', 'salaire_imposable']+\
                        ['revdisp', 'irpp','avantage_qf','impo', 'decote', 'salaire_de_base', 'ir_plaf_qf','salaire_de_base','salcho_imp']


def make_result_dict_single(tax_benefit_system = tax_benefit_system, pickle = False, year_range = range(2012,2016),
                            simulation_var = simulation_var, child_range = range (0, 5) ):

    legislation_var_year = dict()
    for year in year_range:
        simulation = dict()
        for nb_enf in child_range:
            simulation[nb_enf] = make_couple_with_child_scenario(nombre_enfants = nb_enf,
                                                                year = year,
                                                                tax_benefit_system = tax_benefit_system,
                                                               ).new_simulation(debug = False, debug_all = False, trace = False)
        legislation_var = dict()
        for nb_enf, simul in simulation.iteritems():
            var_by_simul = dict()
            temp = dict()
            for var in simulation_var :
                try :
                    temp[var] = simul.calculate_add(var, year)
                except:
                    print 'var {} has failed'.format(var)
            legislation_var[nb_enf] = temp
        print u"ended for year: {}".format(year)
        legislation_var_year[year] = legislation_var

        #print legislation_var_year

    if pickle == True:

        cPickle.dump( legislation_var_year, open( "single_var_{}.p",#.format("bau" #make a test to give the name of the reform to the pickle
                                                  "wb" ) ) #bau = buisness as usual                                # (type(tax_benefit_system) == "openfisca_france.TaxBenefitSystem") * 'bau' + reform.name $ (type(tax_benefit_system) != "openfisca_france.TaxBenefitSystem")

    return  legislation_var_year[year]

if __name__ == '__main__':
    import logging
    log = logging.getLogger(__name__)
    import sys
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    make_result_dict_single(tax_benefit_system = tax_benefit_system, pickle = True, year_range = range(2012,2016),
                            simulation_var = simulation_var, child_range = range (0, 5) )