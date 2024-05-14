
import unittest


from mojo.startup.converters import (
    convert_value_to_bool,
    CSV_TO_LIST_CONVERTER,
    CSV_TO_UNIQUE_LIST_CONVERTER,
    COLSV_TO_LIST_CONVERTER,
    COLSV_TO_UNIQUE_LIST_CONVERTER,
    SCSV_TO_LIST_CONVERTER,
    SCSV_TO_UNIQUE_LIST_CONVERTER,
    SPSV_TO_LIST_CONVERTER,
    SPSV_TO_UNIQUE_LIST_CONVERTER
)


class ConvertToListTests(unittest.TestCase):


    def test_convert_comma_seperated_values_to_list(self):
        value_to_convert = "aa, bb, cc, dd, dd, ee, bb"
        result_list = CSV_TO_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 7, "The resulting list should have been 7 long." 
        return


    def test_convert_colon_seperated_values_to_list(self):
        value_to_convert = "aa: bb: cc: dd: dd: ee: bb"
        result_list = COLSV_TO_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 7, "The resulting list should have been 7 long." 
        return


    def test_convert_semicolon_seperated_values_to_list(self):
        value_to_convert = "aa; bb; cc; dd; dd; ee; bb"
        result_list = SCSV_TO_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 7, "The resulting list should have been 7 long." 
        return


    def test_convert_space_seperated_values_to_list(self):
        value_to_convert = "aa bb cc dd dd ee bb"
        result_list = SPSV_TO_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 7, "The resulting list should have been 7 long." 
        return
    
    def test_convert_space_seperated_values_to_list__dblspace(self):
        value_to_convert = "aa  bb  cc  dd  dd  ee  bb"
        result_list = SPSV_TO_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 7, "The resulting list should have been 7 long." 
        return
    

class ConvertToUniqueListTests(unittest.TestCase):


    def test_convert_comma_seperated_values_to_unique_list(self):
        value_to_convert = "aa, bb, cc, dd, dd, ee, bb"
        result_list = CSV_TO_UNIQUE_LIST_CONVERTER(value_to_convert)
        
        assert len(result_list) == 5, "The resulting length should have been 5 after duplicates were removed."

        return


    def test_convert_colon_seperated_values_to_unique_list(self):
        value_to_convert = "aa: bb: cc: dd: dd: ee: bb"
        result_list = COLSV_TO_UNIQUE_LIST_CONVERTER(value_to_convert)
        
        assert len(result_list) == 5, "The resulting length should have been 5 after duplicates were removed."

        return


    def test_convert_semicolon_seperated_values_to_unique_list(self):
        value_to_convert = "aa; bb; cc; dd; dd; ee; bb"
        result_list = SCSV_TO_UNIQUE_LIST_CONVERTER(value_to_convert)
        
        assert len(result_list) == 5, "The resulting length should have been 5 after duplicates were removed."

        return


    def test_convert_space_seperated_values_to_unique_list(self):
        value_to_convert = "aa bb cc dd dd ee bb"
        result_list = SPSV_TO_UNIQUE_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 5, "The resulting length should have been 5 after duplicates were removed."

        return
    
    def test_convert_space_seperated_values_to_unique_list__dblspace(self):
        value_to_convert = "aa  bb  cc  dd  dd  ee  bb"
        result_list = SPSV_TO_UNIQUE_LIST_CONVERTER(value_to_convert)

        assert len(result_list) == 5, "The resulting length should have been 5 after duplicates were removed."

        return


class ConvertToBoolTests(unittest.TestCase):


    def test_convert_1_and_0_to_bool(self):
        
        result = convert_value_to_bool("1")

        assert result, "The result should have been 'true'."

        result = convert_value_to_bool("0")

        assert not result, "The result should have been 'false'."

        return


    def test_convert_yes_and_no_to_bool_lc(self):
        
        result = convert_value_to_bool("yes")

        assert result, "The result should have been 'true'."

        result = convert_value_to_bool("no")

        assert not result, "The result should have been 'false'."

        return


    def test_convert_true_and_false_to_bool_lc(self):
        
        result = convert_value_to_bool("true")

        assert result, "The result should have been 'true'."

        result = convert_value_to_bool("false")

        assert not result, "The result should have been 'false'."

        return


    def test_convert_yes_and_no_to_bool_mc(self):
        
        result = convert_value_to_bool("Yes")

        assert result, "The result should have been 'true'."

        result = convert_value_to_bool("yEs")

        assert result, "The result should have been 'true'."

        result = convert_value_to_bool("nO")

        assert not result, "The result should have been 'false'."

        result = convert_value_to_bool("No")

        assert not result, "The result should have been 'false'."

        return


    def test_convert_true_and_false_to_bool_mc(self):
        
        result = convert_value_to_bool("True")

        assert result, "The result should have been 'true'."


        result = convert_value_to_bool("False")

        assert not result, "The result should have been 'false'."

        return


    def test_convert_yes_and_no_to_bool_uc(self):
        
        result = convert_value_to_bool("YES")

        assert result, "The result should have been 'true'."

        result = convert_value_to_bool("NO")

        assert not result, "The result should have been 'false'."

        return


    def test_convert_true_and_false_to_bool_uc(self):
        
        result = convert_value_to_bool("TRUE")

        assert result, "The result should have been 'true'."


        result = convert_value_to_bool("FALSE")

        assert not result, "The result should have been 'false'."

        return
    


if __name__ == '__main__':
    unittest.main()
