class ThreeSum(object):
    """Algoritmo para 3SUM"""

    def count(self, a):
        n = len(a)
        count = 0

        for i in range(n):
            #print(i)
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (a[i] + a[j] + a[k]) == 0:
                        count = count + 1

        return count

    def print(self):
        print(self.id)