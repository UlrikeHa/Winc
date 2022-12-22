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
    





# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    
  
   
