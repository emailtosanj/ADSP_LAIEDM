package com.leetcode.hashing;

public class SentencePanagram {

    public boolean checkIfPangram(String sentence) {

        for (int i = 0; i < 26 ; i++)
        {
            char c = (char)('a' + i);

            if(sentence.indexOf(c) == -1)
            {
                return false;
            }
            {
                return false;
            }
        }
        return true;
    }

}
