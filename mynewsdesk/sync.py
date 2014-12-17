from mynewsdesk import models, api

def add_report(report, result):
    report['created'] += result['created']
    report['updated'] += result['updated']
    report['errors'] += result['errors']
    return report

def sync_all(limit=20):
    report = {
        'created': 0,
        'updated': 0,
        'errors': 0
    }

    r = sync_list(models.TYPE_PRESSRELEASE, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_NEWS, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_BLOG_POST, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_CONTACT_PERSON, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_DOCUMENT, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_EVENT, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_IMAGE, limit)
    report = add_report(report, r)

    r = sync_list(models.TYPE_VIDEO, limit)
    report = add_report(report, r)

    return report

def add_link(material, link):
    db_link = models.Link(material=material, url=link['url'], text=link['text'])
    db_link.save()

def get_total_count(service):
    "Fetch total_count by sending a minimal api-request."
    response = api.get_list(type_of_media=service, limit=1)
    if not response or not 'items' in response.keys() or not 'total_count' in response['items']:
        count =  0
    else:
        count = int(response['items']['total_count'])
    return count

def fetch_items(service, limit):
    "Returns a list of all the items available at mynewsdesk"
    total_count = get_total_count(service)
    if total_count < limit:
        limit = total_count

    items = []
    while len(items) < limit:
        response = api.get_list(type_of_media=service, offset=len(items), limit=limit)
        items.extend(response['items']['item'])

    return items

def sync_list(service=models.TYPE_PRESSRELEASE, limit=20):
    item_list = fetch_items(service, limit)
    report = {
        'created': 0,
        'updated': 0,
        'errors': 0
    }
    for item in item_list:
        try:
            try:
                db_item = models.Material.objects.get(id=item['id'], type_of_media=item['type_of_media'])
                report['updated'] += 1
            except models.Material.DoesNotExist:
                db_item = models.Material(id=item['id'], type_of_media=item['type_of_media'])
                report['created'] += 1

            for key, val in item.items():
                if not isinstance(val, list) and not (type(val) is dict):
                    setattr(db_item, key, val)

            db_item.save()

            for key, val in item.items():
                if isinstance(val, list) or (type(val) is dict):
                    if 'channels' == key:
                        for channel in val['channel']:
                            try:
                                db_channel = models.Channel.objects.get(id=channel['id'])
                            except:
                                db_channel = models.Channel(id=channel['id'], title=channel['text'])
                                db_channel.save()
                            db_item.channels.add(db_channel)
                    elif 'event_types' == key:
                        for event_type in val['event_type']:
                            try:
                                db_event_type = models.EventType.objects.get(id=event_type['id'])
                            except:
                                db_event_type = models.EventType(id=event_type['id'], title=event_type['text'])
                                db_event_type.save()
                            db_item.event_types.add(db_event_type)
                    elif 'tags' == key:
                        for tag in val['tag']:
                            try:
                                db_tag = models.Tag.objects.get(name=tag)
                            except:
                                db_tag = models.Tag(name=tag)
                                db_tag.save()
                            db_item.tags.add(db_tag)

                    elif 'links' == key:
                        models.Link.objects.filter(material=db_item).delete()
                        if isinstance(val['link'], list):
                            for link in val['link']:
                                add_link(db_item, link)
                        else:
                            add_link(db_item, val['link'])

                    # TODO: subjects
                    # TODO: geographic_areas
                    # TODO: contact_peoples
                    # TODO: related_items
                    # TODO: instant_messaging
                    # TODO: comments
        except:
            report['errors'] += 1

    return report