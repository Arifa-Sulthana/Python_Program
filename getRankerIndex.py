ranking = ['John', 'Sen', 'Lisa']
ranker_Name = input("Enter Ranker's Name: ").capitalize()
if ranking.__contains__(ranker_Name):
    indexofRanker = ranking.index(ranker_Name) + 1
    print(indexofRanker)
