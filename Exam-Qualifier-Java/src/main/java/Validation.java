public class Validation {
    public boolean isQuestionInputValid(String input){
        if(!input.equalsIgnoreCase("y")) {
            return false;
        }
        if(!input.equalsIgnoreCase("yes")){
            return false;
        }
        if(!input.equalsIgnoreCase("n")){
            return false;
        }
        if(!input.equalsIgnoreCase("no")){
            return false;
        }
        return true;
    }

    public boolean isNumValid(String numTest){
        if(!numTest.matches("[0-9]+")){
            return false;
        }
        return true;
    }

    public boolean isCourseTypeValid(String courseType){
        if(!courseType.equalsIgnoreCase("semester") || !courseType.equalsIgnoreCase("year")){
            return false;
        }
        return true;
    }


}
