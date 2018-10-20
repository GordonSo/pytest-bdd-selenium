How long did you spend on the technical test? What would you add to your solution if you had more time? If you didn't spend much time on the technical test then use this as an opportunity to explain what you would add.
3 hours in total; 1.5 hours to setup the machine, pageobject structure and selenium tests (without BDD)
then I did some research on pytest-bdd (PyCharm's newly supported BDD frameowork since 2018.2)

Given more time, I would look at:
 - Making use of Scenario Outline and Examples to parameterise the 'postcode'
 - Separate the 'browser' fixture into a common module or 'conftest' to allow other scenario to reuse it
 - Parameterise the browser fixture to execute the test on other supported browsers, e.g. Firefox, IE...    
 - Checking if it is necessary to add stricter rules on locators in finding the elements
 - Seeing if there is a better way to integrate Pytest-BDD with PageObject structure
 - Get the tests reporting in Jenkins 

installing pyest-xdist to allow tests to execute in parallel

What do you think is the most interesting trend in test automation?
 > As more company adopts the Agile, TDD; unit tests which are traditionally owned and wrote by the developers 
 > are increasingly becoming contributed to by QAs either through pairing or code reviews 
 > this shows that there is increasing demands in for QA to be proficient in production code's language 
 > and there is a trend that test automation is co-owned.
 
How would you implement test automation in a legacy application? Have you ever had to do this?
 > Legacy application is commonly big and complicated, and implementing test automation can be time consuming.
 > My suggestion would be to identify the critical paths and risky areas where deliver the most business values/ damaging impacts and
 > implement end-to-end tests to ensure that those areas are covered and then iteratively introduce unit tests and acceptance tests for any new modifications.
 > For example, the legacy application will continue to evolve, we can use tools such as sonar to evaluate test coverage and set objectives to improve it by the boy scout rules
 > I had helped my company on a journey to replace a critical business capability from monolithic model into micro-services, I did that by 
 > capturing the expected behaviours and data model from the old model and introduce API tests on the new services to ensure that the behaviours are the same. 
 
How would you improve the customer experience of the Just Eat website?
> The default search order by "best match" when I haven't entered any keywords, maybe 'avg rating' will suggest better recommendation on me (although maybe some A/B test experiment was already done to prove the contrary?)
> Further to search order, a order by 'discount' or 'offers' would be great for customer to evaluate which could be best value for money
> Allow customers to upload pictures of their delivery which can then be linked back to the food menu must allow the next customer to have a richer visual information than only in the star ratings and text based feedback.
> On a similar note, a link to restaurant Instagram's page or hashtag may have similar attraction and helps customer pick and choice restaurants.

Please describe yourself using JSON.
{
	"PersonalInfo": {
		"FullName": "Gordon So",
		"Gender": "M",
		"Interests": ["Technology", "Sports"],
		"Specialities": ["Keen to learn", "Problem solving", "Breaking/ Proving things"]
	},
	"CurrentJob": {
		"Company": "Huddle",
		"Title": "Principle QA",
		"Skills": ["Python", "SQL", "C#", "RabbitMQ", "Redis", "ELK", "Test Automation"],
		"YearsOfService": 4
		"Achievements": ["Huddle of the year award", "Mentoring experience", "Learned lots of skills"]
	}
}