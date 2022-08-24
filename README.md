### Curriculum Logs

##### I have some questions for you that I need answered before the board meeting Thursday afternoon. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
  - we need to group by name (isolates cohort) then value counts on path to show highest/lowest.

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
  - again, like with question one, we are looking for paths by cohort that is not used as much as other.

3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
  - boolean column showing whether row accessed path in between start/end date of student (user id, being unique)  

4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
  - what does it look like when web scraping happens?

5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
  - id users that used both pre 2019, can we see what and how it happened?

6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
  - any hits after their end dates

7. Which lessons are least accessed?
  - value counts again?

8. Anything else I should be aware of?
