package battleship;

import java.io.IOException;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Player1 player1 = new Player1();
        System.out.println("\nPress Enter and pass the move to another player");
        Player2 player2 = new Player2();
        System.out.println("Press Enter and pass the move to another player\n" +
                "...\n");
        System.in.read();
        GameEngine.gameSecondStage(player1, player2);
    }
}

class GameEngine {

    public static final Scanner scanner = new Scanner(System.in);
    public static final List<String> symbol = new ArrayList<>();
    public static final String[] symbols = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};

    public static void gameFirstStage(Player player) {

        boardPrinter(player.board1);

        Ships Aircraft_Carrier = new Aircraft_Carrier();
        while (!shipConstructor(Aircraft_Carrier, player)) ;
        boardPrinter(player.board1);

        Ships Battleship = new Battleship();
        while (!shipConstructor(Battleship, player)) ;
        boardPrinter(player.board1);

        Ships Submarine = new Submarine();
        while (!shipConstructor(Submarine, player)) ;
        boardPrinter(player.board1);

        Ships Cruiser = new Cruiser();
        while (!shipConstructor(Cruiser, player)) ;
        boardPrinter(player.board1);

        Ships Destroyer = new Destroyer();
        while (!shipConstructor(Destroyer, player)) ;
        boardPrinter(player.board1);
    }

    public static void gameSecondStage(Player player1, Player player2) throws IOException {
        while (!isGameFinish(player1) && !isGameFinish(player2)) {
            isShout(player1, player2);
            System.out.println("player 1: " + player1.playerShipsArrayList);
            isShout(player2, player1);
            System.out.println("player2: " + player2.playerShipsArrayList);
        }
        System.out.println("\nYou sank the last ship. You won. Congratulations!");
    }

    public static void boardPrinter(char[][] board) {
        System.out.print("  ");
        for (int i = 1; i <= Constant.BoardSize.length; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        for (int i = 0; i < Constant.BoardSize.length; i++) {
            System.out.print(symbol.get(i) + " ");
            for (int j = 0; j < Constant.BoardSize.length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void board(char[][] board) {
        for (char[] arrays : board) {
            Arrays.fill(arrays, 0, Constant.BoardSize.length, '~');
        }
        for (int i = 0; i < 10; i++) {
            symbol.add(symbols[i]);
        }
    }

    public static boolean shipConstructor(Ships ship, Player player) {
        System.out.println("Enter the coordinates of the " + ship.name + " (" + ship.length + " cells):");
        int lengthOfShip = ship.length;
        int inputLength = 0;
        String[] cell1 = scanner.next().split(""); //strings[0].split("")
        String[] cell2 = scanner.next().split(""); //strings[1].split("");
        int cell1No1;
        int cell1No2;
        int cell2No1;
        int cell2No2;
        if (cell1.length == 2) {
            cell1No1 = symbol.indexOf(cell1[0]);
            cell1No2 = Integer.parseInt(cell1[1]) - 1;
        } else {
            cell1No1 = symbol.indexOf(cell1[0]);
            cell1No2 = Integer.parseInt(cell1[1] + cell1[2]) - 1;
        }
        if (cell2.length == 2) {
            cell2No1 = symbol.indexOf(cell2[0]);
            cell2No2 = Integer.parseInt(cell2[1]) - 1;
        } else {
            cell2No1 = symbol.indexOf(cell2[0]);
            cell2No2 = Integer.parseInt(cell2[1] + cell2[2]) - 1;
        }

        if (cell1[0].equals(cell2[0])) {
            inputLength = Math.abs(cell1No2 - cell2No2) + 1;
            if (inputLength == lengthOfShip) {
                int lower = Math.min(cell1No2, cell2No2);
                int greatest = Math.max(cell1No2, cell2No2);
                if (isTouch(cell1No1, cell2No1, cell1No2, cell2No2, player.board1)) {
                    for (int i = lower; i < greatest + 1; i++) {
                        player.board1[cell1No1][i] = 'O';
                        player.hashMap.put(("" + cell1No1 + i), ship);
                        player.coordinates.add("" + cell1No1 + i);
                        player.playerShipsArrayList.add(ship);
                    }
                } else {
                    System.out.println("Error! You placed it too close to another one. Try again:");
                    return false;
                }
                return true;
            } else {
                System.out.println("Error! Wrong length of the " + ship.name + "! Try again:");
                return false;
            }
        } else if (cell1[1].equals(cell2[1])) {
            inputLength = Math.abs(cell1No1 - cell2No1) + 1;
            if (inputLength == lengthOfShip) {
                int lower = Math.min(cell1No1, cell2No1);
                int greatest = Math.max(cell1No1, cell2No1);
                if (isTouch(cell1No1, cell2No1, cell1No2, cell2No2, player.board1)) {
                    for (int i = lower; i < greatest + 1; i++) {
                        player.board1[i][cell1No2] = 'O';
                        player.hashMap.put(("" + i + cell1No2), ship);
                        player.coordinates.add("" + i + cell1No2);
                        player.playerShipsArrayList.add(ship);
                    }
                } else {
                    System.out.println("Error! You placed it too close to another one. Try again:");
                    return false;
                }
                return true;
            } else {
                System.out.println("Error! Wrong length of the " + ship.name + "! Try again:");
                return false;
            }
        } else {
            System.out.println("Error! Wrong ship location! Try again:");
            return false;
        }
    }

    public static boolean isTouch(int a, int b, int c, int d, char[][] board) {
        int lowerLine = a > b ? b - 1 : a - 1;
        int greatestLine = a > b ? a + 1 : b + 1;
        int lowerColumn = c > d ? d - 1 : c - 1;
        int greatestColumn = c > d ? c + 1 : d + 1;
        if (lowerLine < 0) {
            lowerLine = 0;
        }
        if (greatestLine > Constant.BoardSize.length - 1) {
            greatestLine = Constant.BoardSize.length - 1;
        }
        if (lowerColumn < 0) {
            lowerColumn = 0;
        }
        if (greatestColumn > Constant.BoardSize.length - 1) {
            greatestColumn = Constant.BoardSize.length - 1;
        }
        boolean flag = true;
        for (int i = lowerLine; i < greatestLine + 1; i++) {
            for (int j = lowerColumn; j < greatestColumn + 1; j++) {
                if (board[i][j] == 'O') {
                    flag = false;
                }
            }
        }
        return flag;
    }

    public static boolean isShout(Player player1, Player player2) throws IOException {
        boardPrinter(player2.board2);
        System.out.print("---------------------\n");
        boardPrinter(player1.board1);
        System.out.println(player1.getMsg());
        String[] strings = scanner.next().split("");
        int a;
        int b;
        if (strings.length == 2) {
            a = symbol.indexOf(strings[0]);
            b = Integer.parseInt(strings[1]) - 1;
        } else {
            a = symbol.indexOf(strings[0]);
            b = Integer.parseInt(strings[1] + strings[2]) - 1;
        }
        if (a < 0 || b < 0 || b >= Constant.BoardSize.length) {
            return true;
        }
        if (player2.board1[a][b] == 'O') {
            player2.board1[a][b] = 'X';
            player2.board2[a][b] = 'X';
            Ships tmp = player2.hashMap.get("" + a + b);
            player2.decreaseHealth(tmp);
            tmp.decreaseHealth();
            System.out.println(tmp.name + " " + tmp.getHealth());
            if (tmp.getHealth() > 0) {
                System.out.println("\nYou hit a ship!\n" +
                        "Press Enter and pass the move to another player\n" +
                        "...\n");
                System.in.read();
            } else {
                if (player2.playerShipsArrayList.size() > 0) {
                    System.out.println("\nYou sank a ship! Specify a new target:\n" +
                            "Press Enter and pass the move to another player\n" +
                            "...\n");
                    System.in.read();
                }
            }
            return false;
        } else if (player2.board1[a][b] == 'X') {
            System.out.println("\nYou missed!\n" +
                    "Press Enter and pass the move to another player\n" +
                    "...");
            System.in.read();
            return false;
        }
        player2.board1[a][b] = 'M';
        player2.board2[a][b] = 'M';
        System.out.println("\nYou missed!\n" +
                "Press Enter and pass the move to another player\n" +
                "...\n");
        System.in.read();
        return false;
    }

    public static boolean isGameFinish(Player player) {

        return player.playerShipsArrayList.size() == 0;
    }
}

class Ships {
    String name;
    int length;
    private int health;
    public static ArrayList<Ships> shipsArrayList = new ArrayList<>();

    Ships(String name, int length, int health) {
        this.name = name;
        this.length = length;
        this.health = health;
        shipsArrayList.add(this);
    }


    public int getHealth() {
        return health;
    }

    public boolean decreaseHealth() {
        if (getHealth() > 0) {
            this.health -= 1;
            return true;
        } else {
            return false;
        }
    }
}

class Aircraft_Carrier extends Ships {

    Aircraft_Carrier() {
        super(Constant.AircraftCarrier.name, Constant.AircraftCarrier.length, Constant.AircraftCarrier.health);
    }
}

class Battleship extends Ships {

    Battleship() {
        super(Constant.Battleship.name, Constant.Battleship.length, Constant.Battleship.health);
    }
}

class Submarine extends Ships {

    Submarine() {
        super(Constant.Submarine.name, Constant.Submarine.length, Constant.Cruiser.health);
    }
}

class Cruiser extends Ships {

    Cruiser() {
        super(Constant.Cruiser.name, Constant.Cruiser.length, Constant.Cruiser.health);
    }
}

class Destroyer extends Ships {

    Destroyer() {
        super(Constant.Destroyer.name, Constant.Destroyer.length, Constant.Destroyer.health);
    }
}

enum Constant {
    AircraftCarrier("Aircraft Carrier", 5, 5),
    Battleship("Battleship", 4, 4),
    Submarine("Submarine", 3, 3),
    Cruiser("Cruiser", 3, 3),
    Destroyer("Destroyer", 2, 2),
    BoardSize(10);

    String name;
    int length;
    int health;

    Constant(String name, int length, int health) {
        this.name = name;
        this.length = length;
        this.health = health;
    }

    Constant(int length) {
        this.length = length;
    }
}

class Player {
    public char[][] board1 = new char[Constant.BoardSize.length][Constant.BoardSize.length]; // 1.
    public char[][] board2 = new char[Constant.BoardSize.length][Constant.BoardSize.length]; // 1.
    public HashMap<String, Ships> hashMap = new HashMap<>();
    public ArrayList<Ships> playerShipsArrayList = new ArrayList<>();
    public ArrayList<String> coordinates = new ArrayList<>();

    public String msg;

    public String getMsg() {
        return msg;
    }

    Player() {
        GameEngine.board(board1);
        GameEngine.board(board2);
    }

    public void decreaseHealth(Ships ships) {
        if (playerShipsArrayList.size() > 0) {
            this.playerShipsArrayList.remove(ships);
        }
    }
}

class Player1 extends Player {

    private final String msg = "\nPlayer 1, it's your turn:\n";

    Player1() {
        System.out.println("Player 1, place your ships on the game field\n");
        GameEngine.gameFirstStage(this);
    }

    public String getMsg() {
        return msg;
    }

}

class Player2 extends Player {

    private final String msg = "\nPlayer 2, it's your turn:\n";
    public static Scanner scanner = new Scanner(System.in);

    Player2() {
        System.out.println("...\n" +
                "Player 2, place your ships to the game field\n");
        scanner.nextLine();
        GameEngine.gameFirstStage(this);
    }

    public String getMsg() {
        return msg;
    }
}
