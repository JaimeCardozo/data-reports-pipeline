from datetime import datetime
import calendar

def datesCelebrationList():

    month = datetime.now().strftime("%m")
    dayNow = datetime.now().strftime("%d")
    dayNowInteger = int(dayNow)

    #Este bloque calcula el total de dias del mes actual:
    today = datetime.today()
    year = today.year
    month = today.month
    days_in_month = calendar.monthrange(year, month)[1]



    #Este Bloque calcula los dias que se deben sumar para tener la primera celebracion a partir de la fecha actual
    position_today = datetime.today().weekday()
    dayCelebration = 2 # Posicion del Dia de la celebracion
    diferenteDay = dayCelebration - position_today
    dayAddCelebration = diferenteDay%7

    #Este bloque va a tener los dias de las celebraciones
    celebrationDays = []
    monthCelebration = []
    AllCelebrationDate = [] # --> Aqui van a ir todas las celebraciones (palabra y eucaristia)
    for numberCelebration in range(4):
        positionDay = dayNowInteger + dayAddCelebration + numberCelebration*7
        celebrationDay = positionDay % days_in_month
        #FaltaCalcular el mes, tener en cuenta el total de dias del mes
        celebrationDays.append(celebrationDay)
        if(positionDay>days_in_month):
            monthDate = int(month) + 1
        else:
            monthDate = month
        monthCelebration.append(monthDate)
        AllCelebrationDate.append(f'{celebrationDay}/{monthDate}')

    #Este bloque calcula los dias de las eucaristia
    eucharistDay = []
    diferentEucaristiCelebration = 5-dayCelebration
    for numberEucharist in range(2):
        dayEucharistDay = celebrationDays[numberEucharist]+diferentEucaristiCelebration
        eucharistDay.append(dayEucharistDay)
        AllCelebrationDate.append(f'{dayEucharistDay}/{monthCelebration[numberEucharist]}')

    return AllCelebrationDate