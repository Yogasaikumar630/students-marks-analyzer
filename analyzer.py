{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "46a37372-d97b-4af7-93f7-f247c732bea2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Highest: 90\n",
      "Lowest: 80\n",
      "Average: 85.0\n"
     ]
    }
   ],
   "source": [
    "import csv \n",
    "\n",
    "marks_list=[]\n",
    "\n",
    "with open(\"data.csv\",\"r\") as file:\n",
    "    reader=csv.reader(file)\n",
    "    next(reader)\n",
    "    for row in reader:\n",
    "        marks_list.append(int(row[1]))\n",
    "\n",
    "print(\"Highest:\",max(marks_list))\n",
    "print(\"Lowest:\",min(marks_list))\n",
    "print(\"Average:\",sum(marks_list)/len(marks_list))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}