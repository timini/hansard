BASE_URL="http://www.hansard-archive.parliament.uk/The_Official_Report,_House_of_Lords_(5th_Series)_Vol_1_(Jan_1909)_to_2004//"

for i in {1..623}
do
    n=`printf %04d%s $i`
    wget $BASE_URL'S5LV'$n'P0.zip'
done
