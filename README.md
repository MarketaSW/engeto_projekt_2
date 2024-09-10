# Tic-tac-toe (Piškvorky)
Druhý projekt v Python akademii Engeto

Cílem této hry je umístit 3 hrací kameny (křížek X nebo kolečko O), a to horizontálně, vertikálně nebo diagonálně. Jde o hru pro dva hráče (příp. počítač).

### Co umí?

![welcome](/assets/welcome.png)
- pozdravit uživatele
- vypsat pravidla hry
- zeptat se na jména hráčů
- spustit hru
  - zobrazí hrací plochu,
  - vyzve prvního hráče, aby zvolil pozici pro umístění hracího kamene
  - pokud hráč zadá jiné číslo, než je nabídka hracího pole, program jej upozorní
  - pokud hráč zadá jiný vstup, než číselný, program jej opět upozorní
  - pokud se na vybraném poli nachází hrací kámen druhého hráče, program jej upozorní, že je pole obsazené
  - jakmile hráč úspěšně vybere pole, zobrazí nový stav hrací plochy
    
Program vyhodnocuje, jestli horizontálně/vertikálně/diagonálně není některý hrací kámen třikrát. Pokud ano, vyhrává hráč, kterému tyto tři kameny patří, pokud nezbývá žádné volné hrací pole a žádný hráč nevyhrál, jde o remízu.

![end of game](/assets/win.png)
