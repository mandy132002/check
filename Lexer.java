import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Lexer {
    public static void main(String[] args) {
        String fileName = "input.txt";
        String line = null;
        StringBuilder stringBuilder = new StringBuilder();

        try (BufferedReader bufferedReader = new BufferedReader(new FileReader(fileName))) {
            while ((line = bufferedReader.readLine()) != null) {
                stringBuilder.append(line).append("\n");
            }
        } catch (IOException e) {
            System.err.format("IOException: %s%n", e);
        }

        String code = stringBuilder.toString();
        Pattern pattern = Pattern.compile("\\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\\b|[A-Za-z_][A-Za-z0-9_]*|\\b\\d+(\\.\\d+)?\\b|[+\\-*/]|=|;|\\(|\\)");
        Matcher matcher = pattern.matcher(code);
        while (matcher.find()) {
            String match = matcher.group();
            if (match.matches("\\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\\b")) {
                System.out.println("KEYWORD: " + match);
            } else if (match.matches("[A-Za-z_][A-Za-z0-9_]*")) {
                System.out.println("VARIABLE: " + match);
            } else if (match.matches("\\b\\d+(\\.\\d+)?\\b")) {
                System.out.println("NUMBER: " + match);
            } else if (match.matches("[+\\-*/]")) {
                System.out.println("OPERATOR: " + match);
            } else if (match.equals("=")) {
                System.out.println("ASSIGNMENT: " + match);
            } else if (match.equals(";")) {
                System.out.println("SEMICOLON: " + match);
            }
            else if (match.equals("(")) {
                System.out.println("LEFT PARENTHESIS: " + match);
            }
            else if (match.equals(")")) {
                System.out.println("RIGHT PARENTHESIS: " + match);
            }
        }
    }
}
