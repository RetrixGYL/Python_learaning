immutable_var=1,2,"rock"
print(immutable_var)
#immutable_var[0]="imago" - typle неизменяемый тип коллекции, поэтому команда не работает, исключением является редактирование списка внутри кортежа, а также операции суммирование и умножение
mutable_list=[1,2,3,"paper"]
mutable_list[0]=666
print(mutable_list)
