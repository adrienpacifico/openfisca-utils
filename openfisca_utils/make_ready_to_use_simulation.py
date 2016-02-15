__author__ = 'adrienpacifico'


from openfisca_utils import make_ready_to_use_scenario

def make_ready_to_use_simulation(year = None, couple = True):
    if couple == True:
        scenario = make_ready_to_use_scenario.make_couple_with_child_scenario(year = year)
    if couple == False:
        scenario = make_ready_to_use_scenario.make_single_with_child_scenario(year = year)
    return scenario.new_simulation()
