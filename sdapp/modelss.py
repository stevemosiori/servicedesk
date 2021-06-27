from django.db import models

class AgentActivity(models.Model):
    agent = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey('Ticket', on_delete=models.DO_NOTHING)
    agent_name = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    thread_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'agent_activity'


class Announcement(models.Model):
    group = models.ForeignKey('SupportGroup', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    promo_text = models.CharField(max_length=255)
    promo_tag = models.CharField(max_length=255)
    tag_color = models.CharField(max_length=255, blank=True, null=True)
    link_text = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    is_active = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'announcement'


class MigrationVersions(models.Model):
    version = models.CharField(primary_key=True, max_length=14)
    executed_at = models.DateTimeField()

    class Meta:
        db_table = 'migration_versions'


class Recaptcha(models.Model):
    site_key = models.CharField(max_length=255, blank=True, null=True)
    secret_key = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'recaptcha'

class AdminSupportGroups(models.Model):
    adminuserinstanceid = models.OneToOneField('UserInstance', on_delete=models.DO_NOTHING, db_column='adminUserInstanceId', primary_key=True)  # Field name made lowercase.
    supportgroupid = models.ForeignKey('SupportGroup', on_delete=models.DO_NOTHING, db_column='supportGroupId')  # Field name made lowercase.

    class Meta:
        db_table = 'admin_support_groups'
        unique_together = (('adminuserinstanceid', 'supportgroupid'),)


class Article(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    viewed = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    stared = models.IntegerField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'article'


class ArticleCategory(models.Model):
    article_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        db_table = 'article_category'


class ArticleFeedback(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True)
    is_helpful = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'article_feedback'


class ArticleHistory(models.Model):
    article_id = models.IntegerField()
    user_id = models.IntegerField()
    content = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'article_history'


class ArticleTags(models.Model):
    article_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        db_table = 'article_tags'


class ArticleViewLog(models.Model):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING, blank=True, null=True)
    viewed_at = models.DateTimeField()

    class Meta:
        db_table = 'article_view_log'


class EmailTemplates(models.Model):
    user = models.ForeignKey('UserInstance', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=191)
    subject = models.CharField(max_length=191)
    message = models.TextField()
    template_type = models.CharField(max_length=255, blank=True, null=True)
    is_predefined = models.IntegerField()

    class Meta:
        db_table = 'email_templates'


class LeadSupportTeams(models.Model):
    leaduserinstanceid = models.OneToOneField('UserInstance', on_delete=models.DO_NOTHING, db_column='leadUserInstanceId', primary_key=True)  # Field name made lowercase.
    supportteamid = models.ForeignKey('SupportTeam', on_delete=models.DO_NOTHING, db_column='supportTeamId')  # Field name made lowercase.

    class Meta:
        db_table = 'lead_support_teams'
        unique_together = (('leaduserinstanceid', 'supportteamid'),)


class PreparedResponseSupportGroups(models.Model):
    group = models.ForeignKey('SupportGroup', on_delete=models.DO_NOTHING)
    savedreply = models.OneToOneField('PreparedResponses', on_delete=models.DO_NOTHING, db_column='savedReply_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'prepared_response_support_groups'
        unique_together = (('savedreply', 'group'),)


class PreparedResponseSupportTeams(models.Model):
    subgroup = models.ForeignKey('SupportTeam', on_delete=models.DO_NOTHING)
    savedreply = models.OneToOneField('PreparedResponses', on_delete=models.DO_NOTHING, db_column='savedReply_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'prepared_response_support_teams'
        unique_together = (('savedreply', 'subgroup'),)


class PreparedResponses(models.Model):
    user = models.ForeignKey('UserInstance', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    actions = models.TextField()
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'prepared_responses'


class RelatedArticles(models.Model):
    article_id = models.IntegerField()
    related_article_id = models.IntegerField()

    class Meta:
        db_table = 'related_articles'


class SavedFilters(models.Model):
    user = models.ForeignKey('UserInstance', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=191)
    filtering = models.TextField(blank=True, null=True)
    route = models.CharField(max_length=190, blank=True, null=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'saved_filters'


class SavedReplies(models.Model):
    user = models.ForeignKey('UserInstance', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    template_id = models.IntegerField(blank=True, null=True)
    is_predefind = models.IntegerField(blank=True, null=True)
    message_inline = models.TextField(blank=True, null=True)
    template_for = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'saved_replies'


class SavedRepliesGroups(models.Model):
    group = models.ForeignKey('SupportGroup', on_delete=models.DO_NOTHING)
    savedreply = models.OneToOneField(SavedReplies, on_delete=models.DO_NOTHING, db_column='savedReply_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'saved_replies_groups'
        unique_together = (('savedreply', 'group'),)


class SavedRepliesTeams(models.Model):
    subgroup = models.ForeignKey('SupportTeam', on_delete=models.DO_NOTHING)
    savedreply = models.OneToOneField(SavedReplies, on_delete=models.DO_NOTHING, db_column='savedReply_id', primary_key=True)  # Field name made lowercase.

    class Meta:
        db_table = 'saved_replies_teams'
        unique_together = (('savedreply', 'subgroup'),)


class SolutionCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    sorting = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField()
    status = models.IntegerField(blank=True, null=True)
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'solution_category'


class SolutionCategoryMapping(models.Model):
    solution_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        db_table = 'solution_category_mapping'


class Solutions(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    visibility = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    solution_image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'solutions'



class SupportGroupsTeams(models.Model):
    supportgroup = models.OneToOneField(SupportGroup, on_delete=models.DO_NOTHING, db_column='supportGroup_id', primary_key=True)  # Field name made lowercase.
    supportteam = models.ForeignKey('SupportTeam', on_delete=models.DO_NOTHING, db_column='supportTeam_id')  # Field name made lowercase.

    class Meta:
        db_table = 'support_groups_teams'
        unique_together = (('supportgroup', 'supportteam'),)


class SupportLabel(models.Model):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=191)
    color_code = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'support_label'


class SupportPrivilege(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField()
    privileges = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'support_privilege'


class SupportRole(models.Model):
    code = models.CharField(unique=True, max_length=191)
    description = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'support_role'

class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tag'


class Thread(models.Model):
    ticket = models.ForeignKey('Ticket', on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True)
    source = models.CharField(max_length=191)
    message_id = models.TextField(blank=True, null=True)
    thread_type = models.CharField(max_length=191)
    created_by = models.CharField(max_length=191)
    cc = models.TextField(blank=True, null=True)
    bcc = models.TextField(blank=True, null=True)
    reply_to = models.TextField(blank=True, null=True)
    delivery_status = models.CharField(max_length=255, blank=True, null=True)
    is_locked = models.IntegerField()
    is_bookmarked = models.IntegerField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    agent_viewed_at = models.DateTimeField(blank=True, null=True)
    customer_viewed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'thread'






class TicketRating(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING, blank=True, null=True)
    stars = models.IntegerField()
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'ticket_rating'


class TicketsCollaborators(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tickets_collaborators'
        unique_together = (('ticket', 'user'),)


class TicketsLabels(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.DO_NOTHING, primary_key=True)
    label = models.ForeignKey(SupportLabel, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tickets_labels'
        unique_together = (('ticket', 'label'),)


class TicketsTags(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tickets_tags'
        unique_together = (('ticket', 'tag'),)





class UserInstance(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    source = models.CharField(max_length=191)
    skype_id = models.CharField(max_length=191, blank=True, null=True)
    contact_number = models.CharField(max_length=191, blank=True, null=True)
    designation = models.CharField(max_length=191, blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    profile_image_path = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField()
    is_verified = models.IntegerField()
    is_starred = models.IntegerField()
    ticket_access_level = models.CharField(max_length=32, blank=True, null=True)
    supportrole = models.ForeignKey(SupportRole, on_delete=models.DO_NOTHING, db_column='supportRole_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'user_instance'


class UserSupportGroups(models.Model):
    userinstanceid = models.OneToOneField(UserInstance, on_delete=models.DO_NOTHING, db_column='userInstanceId', primary_key=True)  # Field name made lowercase.
    supportgroupid = models.ForeignKey(SupportGroup, on_delete=models.DO_NOTHING, db_column='supportGroupId')  # Field name made lowercase.

    class Meta:
        db_table = 'user_support_groups'
        unique_together = (('userinstanceid', 'supportgroupid'),)


class UserSupportPrivileges(models.Model):
    userinstanceid = models.OneToOneField(UserInstance, on_delete=models.DO_NOTHING, db_column='userInstanceId', primary_key=True)  # Field name made lowercase.
    supportprivilegeid = models.ForeignKey(SupportPrivilege, on_delete=models.DO_NOTHING, db_column='supportPrivilegeId')  # Field name made lowercase.

    class Meta:
        db_table = 'user_support_privileges'
        unique_together = (('userinstanceid', 'supportprivilegeid'),)


class UserSupportTeams(models.Model):
    userinstanceid = models.OneToOneField(UserInstance, on_delete=models.DO_NOTHING, db_column='userInstanceId', primary_key=True)  # Field name made lowercase.
    supportteamid = models.ForeignKey(SupportTeam, on_delete=models.DO_NOTHING, db_column='supportTeamId')  # Field name made lowercase.

    class Meta:
        db_table = 'user_support_teams'
        unique_together = (('userinstanceid', 'supportteamid'),)


class Website(models.Model):
    name = models.CharField(max_length=191)
    code = models.CharField(unique=True, max_length=191)
    logo = models.CharField(max_length=191, blank=True, null=True)
    theme_color = models.CharField(max_length=191)
    favicon = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.IntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=191, blank=True, null=True)
    timeformat = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'website'


class WebsiteKnowledgebase(models.Model):
    website = models.ForeignKey(Website, on_delete=models.DO_NOTHING, db_column='website', blank=True, null=True)
    status = models.CharField(max_length=255)
    brand_color = models.CharField(max_length=255)
    page_background_color = models.CharField(max_length=255)
    header_background_color = models.CharField(max_length=255, blank=True, null=True)
    link_color = models.CharField(max_length=255, blank=True, null=True)
    article_text_color = models.CharField(max_length=255, blank=True, null=True)
    ticket_create_option = models.CharField(max_length=255)
    site_description = models.CharField(max_length=1000, blank=True, null=True)
    meta_description = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    homepage_content = models.CharField(max_length=255, blank=True, null=True)
    white_list = models.TextField(blank=True, null=True)
    black_list = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    broadcast_message = models.TextField(blank=True, null=True)
    disable_customer_login = models.IntegerField()
    script = models.TextField(blank=True, null=True)
    custom_css = models.TextField(blank=True, null=True)
    is_active = models.IntegerField()
    header_links = models.TextField(blank=True, null=True)
    footer_links = models.TextField(blank=True, null=True)
    banner_background_color = models.CharField(max_length=255, blank=True, null=True)
    link_hover_color = models.CharField(max_length=255, blank=True, null=True)
    login_required_to_create = models.IntegerField(blank=True, null=True)
    remove_customer_login_button = models.IntegerField(blank=True, null=True)
    remove_branding_content = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'website_knowledgebase'


class Workflow(models.Model):
    name = models.CharField(max_length=191)
    description = models.TextField(blank=True, null=True)
    conditions = models.TextField()
    actions = models.TextField()
    sort_order = models.IntegerField(blank=True, null=True)
    is_predefind = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'workflow'


class WorkflowEvents(models.Model):
    workflow = models.ForeignKey(Workflow, on_delete=models.DO_NOTHING, blank=True, null=True)
    event_id = models.IntegerField()
    event = models.CharField(max_length=191)

    class Meta:
        db_table = 'workflow_events'
