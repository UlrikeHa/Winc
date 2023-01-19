from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"



def unique_koala_facts(int):
    facts_list = []
    wiederholung = 0    
    while len(facts_list) < int and wiederholung < 1000:
        new_fact = random_koala_fact()
        if new_fact not in facts_list:
            facts_list.append(new_fact)
        wiederholung += 1
    return facts_list
    
def num_joey_facts():
    first_joey_fact = []
    counter = 0
    list_joey_facts = []
    while counter < 10:
        new_fact = random_koala_fact()
        if "joey" in new_fact:
            if new_fact not in list_joey_facts:
                list_joey_facts.append(new_fact)
            if counter == 0:
                first_joey_fact.append(new_fact)
            if new_fact in first_joey_fact:
                counter += 1   
    return len(list_joey_facts)

def koala_weight():
    weight_not_found = True
    while weight_not_found == True:
        new_fact = random_koala_fact()
        if "kg" in new_fact:
            cut = new_fact[: new_fact.find("kg")]
            weight = cut[cut.rfind(" ") + 1:]
            weight_not_found = False
    return int(weight)



# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    print(num_joey_facts())
    print(koala_weight())  
  
   
