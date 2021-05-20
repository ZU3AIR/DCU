public class FirstShallBeLast {
    public static String firstShallBeLast(String word)
    {
        int wordlength = word.length();
        return ("Test.firstShallBeLast(" + word + ") is " + word.substring(wordlength-1) + word.substring(1, wordlength) + word.substring(0));
    }
}
