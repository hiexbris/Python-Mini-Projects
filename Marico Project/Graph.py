import pandas as pd


class Grapher:

    def __init__(self, sheet):
        #self.bci_summary = sheet['BCI Summary']
        self.ingredientsXBC = sheet['Ingredients X BC']
        #self.band = sheet['Prices, Weights and Packaging']
        #self.brandwise = sheet['Brandwise Attributes']

    def benefits(self, cap, no_of_brands):
        benefits = {}
        row_index, col_index = self.bci_summary.where(self.bci_summary == 'Benefits').stack().index[0]
        if no_of_brands != 0:
            cap = self.bci_summary.at[row_index+1+no_of_brands, col_index+2]*100
        for i in range(row_index+1, 15):
            share = (self.bci_summary.at[i, col_index+2]) * 100
            if isinstance(share, float) and not pd.isna(share):
                if share >= cap and isinstance(self.bci_summary.at[i, col_index], str):
                    share = round(float(share))
                    benefits[(self.bci_summary.at[i, col_index])] = share

        return benefits

    def claims(self, cap, no_of_brands):
        row_index, col_index = self.bci_summary.where(self.bci_summary == 'Claims').stack().index[0]
        if no_of_brands != 0:
            cap = self.bci_summary.at[row_index+1+no_of_brands, col_index+2]*100
        claims = {}
        for i in range(row_index+1, 15):
            share = (self.bci_summary.at[i, col_index+2]) * 100
            if isinstance(share, float) and not pd.isna(share):
                if share >= cap and isinstance(self.bci_summary.at[i, col_index], str):
                    share = round(float(share))
                    claims[(self.bci_summary.at[i, col_index])] = share

        return claims

    def ingredient(self, cap, no_of_brands):
        row_index, col_index = self.bci_summary.where(self.bci_summary == 'Ingredients').stack().index[0]
        if no_of_brands != 0:
            cap = self.bci_summary.at[row_index+1+no_of_brands, col_index+2]*100
        ingredient = {}
        for i in range(row_index+1, 20):
            share = (self.bci_summary.at[i, col_index+2]) * 100
            if isinstance(share, float) and not pd.isna(share):
                if share >= cap  and isinstance(self.bci_summary.at[i, col_index], str):
                    share = round(float(share))
                    ingredient[self.bci_summary.at[i, col_index]] = share

        return ingredient

    def benefits_with_ingredients(self):
        ingredient = {}
        index_of_gap_benefits = self.ingredientsXBC.iloc[1].index[self.ingredientsXBC.iloc[1].isna()].tolist()
        for i in range(1, 8):
            value = self.ingredientsXBC.at[i, 0]
            ingredient[self.ingredientsXBC.at[i, 1]] = [round(value)]
        benefits_percentage = {}
        for i in range(1, 8):
            total = 0
            for t in range(2, index_of_gap_benefits[0]):
                if not pd.isna(self.ingredientsXBC.at[i, t]):
                    total += self.ingredientsXBC.at[i, t]
            for t in range(2, index_of_gap_benefits[0]):
                if not pd.isna(self.ingredientsXBC.at[i, t]):
                    value = self.ingredientsXBC.at[i, t]*self.ingredientsXBC.at[i, 0]/total
                    benefits_percentage[self.ingredientsXBC.at[0, t]] = round(value, 2)
            ingredient[self.ingredientsXBC.at[i, 1]].append(benefits_percentage.copy())

        return ingredient

    def claims_with_ingredients(self):
        ingredient = {}
        nan_list_row = self.ingredientsXBC.iloc[1].index[self.ingredientsXBC.iloc[1].isna()].tolist()
        index_of_gap_claims = len(self.ingredientsXBC.columns)
        for i in range(1, 8):
            value = self.ingredientsXBC.at[i, 0]
            ingredient[self.ingredientsXBC.at[i, 1]] = [round(value)]
        claims_percentage = {}
        for i in range(1, 8):
            total = 0
            for t in range(nan_list_row[0]+1, index_of_gap_claims):
                if not pd.isna(self.ingredientsXBC.at[i, t]):
                    total += self.ingredientsXBC.at[i, t]
            for t in range(nan_list_row[0]+1, index_of_gap_claims):
                if not pd.isna(self.ingredientsXBC.at[i, t]):
                    value = self.ingredientsXBC.at[i, t] * self.ingredientsXBC.at[i, 0]/ total
                    claims_percentage[self.ingredientsXBC.at[0, t]] = round(value, 2)
            ingredient[self.ingredientsXBC.at[i, 1]].append(claims_percentage.copy())

        return ingredient

    def branddata(self, cap, no_of_brands, col_index_heading):
        dict = {}
        row_index_brand, col_index_brand = self.brandwise.where(self.brandwise == 'Brand').stack().index[0]
        if no_of_brands == 0:
            for i in range(row_index_brand+1, 30):
                share = self.brandwise[i, 3]*100
                if share >= cap:
                    no_of_brands += 1
                else:
                    break
        for i in range(row_index_brand+1, row_index_brand+no_of_brands+1):
            if not pd.isna(self.brandwise.at[i, col_index_brand]):
                value = self.brandwise.at[i, col_index_heading]
                dict[self.brandwise.at[i, col_index_brand]] = round(value, 2)
            else:
                no_of_brands += 1

        return dict

    def branddata_percent(self, cap, no_of_brands, col_index_heading):
        row_index_brand, col_index_brand = self.brandwise.where(self.brandwise == 'Brand').stack().index[0]
        if no_of_brands == 0:
            for i in range(row_index_brand+1, 30):
                share = self.brandwise[i, 3]*100
                if share >= cap:
                    no_of_brands += 1
                else:
                    break
        dict = {}
        for i in range(row_index_brand+1, row_index_brand+no_of_brands+1):
            if not pd.isna(self.brandwise.at[i, col_index_brand]):
                share = self.brandwise.at[i, col_index_heading]*100
                dict[self.brandwise.at[i, col_index_brand]] = round(share, 2)
            else:
                no_of_brands += 1

        return dict

    def band_new(self, column_list):
        dict = {}
        for i in range(1, 30):
            if self.band.at[i, column_list] != 'Grand Total':
                dict[self.band.at[i, column_list]] = self.band.at[i, column_list+3]*100
            else:
                break

        return dict