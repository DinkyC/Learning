import statistics as st
import standard_dev as sd
import zscore as zs

smoker = [4.5, 5.4, 5.9, 6.1, 6.6, 6.6, 7.1, 7.2, 7.6, 8.0]

non_smoker = [5.3, 5.6, 6.1, 6.5, 6.7, 7.1, 7.6, 7.9, 8.3, 8.6, 9.2]

lst = [24, 18, 6, 11, 43, 35]

mns = st.mean(smoker)

mn = st.mean(non_smoker)
standard_nonsmoker = sd.standard_dev(non_smoker)
standard_smoker = sd.standard_dev(smoker)
# print("Standard Deviation: ", standard_smoker)

z_for_nine = zs.zscore(4, mn, standard_nonsmoker)
# print("z-score at nine pounds for non-smokers: ", z_for_nine)

z = zs.zscore(74, 48, 12.8)
print("z-score at nine pounds for smokers: ", z)

print(st.mean(lst))

print(sd.standard_dev(lst))

