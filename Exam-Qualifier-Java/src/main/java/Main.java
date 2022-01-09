import java.util.List;
import java.util.Scanner;
public class Main {
    //Scanner sc = new Scanner(System.in);
    public static String getName(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first name(s): ");
        return sc.next();
    }

    public static String getSurname(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter surname: ");
        return sc.next();
    }

    public static String getCourseType(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter course type (year/semester): ");
        return sc.next();
    }

    public static String getModuleName(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter module you are studying: ");
        return sc.next();
    }

    public static String getQualification(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter qualification you are studying for: ");
        return sc.next();
    }

    public static String areTestsWritten(String courseType){
        return null;
    }

    public static String areProjectsWritten(String courseType){
        return null;
    }

    public static String arePresentationsWritten(String courseType){
        return null;
    }

    public static int numTests(){
        Scanner sc = new Scanner(System.in);
        String numTest;
        System.out.println("How many tests have you written?: ");
        numTest = sc.next();
        return Integer.parseInt(numTest);
    }

    public static int numProjects(){
        Scanner sc = new Scanner(System.in);
        String numProjects;
        System.out.println("How many projects have you done?: ");
        numProjects = sc.next();
        return Integer.parseInt(numProjects);
    }

    public static int numPresentations(){
        Scanner sc = new Scanner(System.in);
        String numPresentations;
        System.out.println("How many presentations have you done?: ");
        numPresentations = sc.next();
        return Integer.parseInt(numPresentations);
    }

    public static List<Integer> getTestList(int testCount){
        return null;
    }

    public static List<Integer> getProjectList(int projectCount){
        return null;
    }

    public static List<Integer> getPresentationList(int presentationCount){
        return null;
    }

    public static void display(){
        String name;
        String surname;

        int totMark;
        int count;
        int avgMark;

        int avgTest;
        int avgProject;
        int avgPresentation;

        name = getName();
        surname = getSurname();


    }

    public static void main(String[] args){
        display();
    }
}
