#!/usr/bin/env bash
for j in {0..4}
do
    for i in {5..15}
    do
	    cd /home/student/code
	    make clean
	    make
	    cd ../fold$j
	    sed -i "s/NHY 5/NHY $i/g" Options.txt
	    sed -i "s/NF 5/NF $i/g" Options.txt
	    sed -i "s/NHF 5/NHF $i/g" Options.txt
	    ../code/Train Options.txt train.dataset ./
	    cd ../code
	    make -f makefile.mcc
	    cd ../fold$j
	    echo "NHY/NF/NHF=$i" >> ../results/fold_$j.txt
	    sed -i "s/NHY $i/NHY 5/g" Options.txt
	    sed -i "s/NF $i/NF 5/g" Options.txt
	    sed -i "s/NHF $i/NHF 5/g" Options.txt
	    ../code/Predict_wholeset_mcc Models.txt test.dataset ./ >> ../results/fold_$j.txt
	    cd ..
    done
done
