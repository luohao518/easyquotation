import easyquotation
import time
# import winsound
from easyutils import timeutils 

def queryCb():
	
    quotation = easyquotation.use('jsl')  # ['jsl']
    
    data = quotation.cb()

    watchEtfmoneys = ['110030']

    price = 112.00
    
    price2 = 112.60
        
    print(data)
    for bond_id, cell in data.items():
        if cell["bond_id"] in watchEtfmoneys:
            if cell["bond_id"]==watchEtfmoneys[0]:
                
                if float(cell["price"]) <= price2:
                     print(cell["bond_id"] + '    :    ' + cell["price"])
                    #  winsound.Beep(2800, 500)
                    
            elif float(cell["price"]) <= price:
                print(cell["bond_id"] + '    :    ' + cell["price"])
                # winsound.Beep(2800, 500)
            else:
                pass
                
def check_tradetime():
    
    if(timeutils.is_holiday_today()):
        print(u'2')
        return 2
    
    elif timeutils.is_tradetime_now():
        return 0
    
    else:
        if(timeutils.calc_next_trade_time_delta_seconds()>1.5*60*60):
            print(u'1')
            return 2
        else:
            return 1
            
def main_process():
    
    SLEEP_TIME=30
    IS_TEST=0
    
    if(not IS_TEST or check_tradetime() == 1):
        for i in range(int((4*60*60)/SLEEP_TIME)):
            queryCb()
            print('---------------------------')
            time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main_process()
        


