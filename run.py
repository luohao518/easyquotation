import easyquotation
import time
import winsound
from easyutils import timeutils 

def queryEtfmoneys():


        
    # quotation = easyquotation.use('sina')
    # a=quotation.stocks('511910')
	
    quotation = easyquotation.use('jsl')  # ['jsl']
    # a=quotation.fundarb('luohao', 'wangyan', avolume=100, bvolume=100, ptype='price')
    
    # a=quotation.etfindex(index_id="", min_volume=0, max_discount=None, min_discount=None)
    
    
    data = quotation.etfmoney()

    watchEtfmoneys = ['511990','511900','511980']

    price = 99.989
    
    price2 = 102.075
    
    for fund_id, cell in data.items():
        if cell["fund_id"] in watchEtfmoneys:
            if cell["fund_id"]==watchEtfmoneys[0]:
                #银华日利
                if float(cell["price"]) <= price2:
                     print(cell["fund_id"] + '    :    ' + cell["price"])
                     winsound.Beep(2800, 500)
                    
            elif float(cell["price"]) <= price:
                print(cell["fund_id"] + '    :    ' + cell["price"])
                winsound.Beep(2800, 500)
            else:
                pass
                
def check_tradetime():
    
    if(timeutils.is_holiday_today()):
        print(u'节假日，股市休市.')
        return 2
    
    elif timeutils.is_tradetime_now():
        return 0
    
    else:
        if(timeutils.calc_next_trade_time_delta_seconds()>1.5*60*60):
            print(u'非交易时间。')
            return 2
        else:
            return 1
            
def main_process():
    
    SLEEP_TIME=30
    IS_TEST=0
    
    if(not IS_TEST or check_tradetime() == 1):
        for i in range(int((4*60*60)/SLEEP_TIME)):
            queryEtfmoneys()
            print('---------------------------')
            time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main_process()
        


