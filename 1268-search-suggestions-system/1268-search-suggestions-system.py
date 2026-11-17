class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        # print(products)
        result = []
        
        i=1
        while i<=len(searchWord):
            heap = []
            for pro in products:
                # print(searchWord[:i],pro)
                # input()
                if pro.startswith(searchWord[:i]):
                    if len(heap)!=3:
                        heap.append(pro)
                    else:
                        break
                        
            result.append(heap)
            i+=1
        return result