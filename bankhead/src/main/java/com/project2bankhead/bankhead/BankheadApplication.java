 package com.project2bankhead.bankhead;


 import java.util.ArrayList;
 import java.util.HashMap;
 import java.util.List;
 import java.util.Map;
 import java.util.Optional;
 
 import org.springframework.web.bind.annotation.GetMapping;
 import org.springframework.web.bind.annotation.PathVariable;
 import org.springframework.web.bind.annotation.RequestMapping;
 import org.springframework.web.bind.annotation.RestController;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class BankheadApplication {

	public static void main(String[] args) {
		SpringApplication.run(BankheadApplication.class, args);
		Database.loadData();
    }
    
    @RestController
    @RequestMapping(value ="/loadData", method=RequestMethod.GET)
    public class RestApi {
        
        @GetMapping
        public Iterable<String> getLoadData() {
            return Database.loadData("");
        }
    
        @GetMapping("/{id}")
        public Optional<String> getloadDataById(@PathVariable Integer id) {
            List<Map<String, Objects>>loadData = new ArrayList<> ();
            for (String loadData: Database.policies) {
                if (loadData.policesgetId().equals(id)) {
                    return Optional.of(loadData);
                }
            }
            return Optional.empty();
        }   
        private Map<String, Object> maploadData(loadData InsuranceCLaim)
        {
            Map<String, Object> loadDataMap = new HashMap<>();
            loadDataMap.put("id", InsurancePolicy.getId());
            loadDataMap.put("name", InsurancePolicy.getName());
            loadDatamap.put("description", InsuranceCLaim.getDescription());
            return loadDataMap;
        }   
}}




