public class Average_Temperature {
    
    String city;
    int temperature;
    private static final int citiesLength = 10;
    
    private Average_Temperature(String city, int temperature) {
        this.city = city;
        this.temperature = temperature;
    }
    
    public static void main(String[] args) {
        
        Average_Temperature[] temp = new Average_Temperature[citiesLength];
        
        System.out.println("Average July Temperatures by City");
        
        addCites(temp);
        sortTemp(temp);
        
        for (Average_Temperature sorted_Temp : temp) {
            if (sorted_Temp != null) {
                System.out.println(sorted_Temp.city + ": " + sorted_Temp.temperature);
            }
        }
    }
    
    static void addCites(Average_Temperature[] temp) {
        temp[0] = new Average_Temperature("New Delhi", 45);
        temp[1] = new Average_Temperature("Bangalore", 37);
        temp[2] = new Average_Temperature("Faridabad", 41);
        temp[3] = new Average_Temperature("Guwahati", 34);
        temp[4] = new Average_Temperature("Thiruvanthapuram", 37);
        temp[5] = new Average_Temperature("Pune", 36);
        temp[6] = new Average_Temperature("Ladakh", 30);
        temp[7] = new Average_Temperature("Chandigarh", 39);
        temp[8] = new Average_Temperature("Jaipur", 46);
        temp[9] = new Average_Temperature("Noida", 40);
    }
    
    static void sortTemp(Average_Temperature[] temp) {
        
        for (int i = 0; i < citiesLength; i++) {
            int firstIndexTemp = i;
            
            for (int j = i + 1; j < citiesLength; j++) {
                if (temp[firstIndexTemp].temperature < temp[j].temperature) {
                    firstIndexTemp = j;
                }
            }
            
            if (firstIndexTemp != i) {
                int temperature_swap = temp[firstIndexTemp].temperature;
                temp[firstIndexTemp].temperature = temp[i].temperature;
                temp[i].temperature = temperature_swap;

                String city_swap = temp[firstIndexTemp].city;
                temp[firstIndexTemp].city = temp[i].city;
                temp[i].city = city_swap;
            }
        }
    }
}