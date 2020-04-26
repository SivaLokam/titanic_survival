REM set TRAINING_DATA=input/train_folds.csv
REM set TEST_DATA=input/test.csv

REM set MODEL=%1


REM set FOLD=0 && python -m src.train
REM set FOLD=1 && python -m src.train
REM set FOLD=2 && python -m src.train
REM set FOLD=3 && python -m src.train
REM set FOLD=4 && python -m src.train

python -m src.create_folds
