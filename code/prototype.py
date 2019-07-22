class Website: 
    def __init__(self, name, domain, description, author, **kwargs): 
        '''Examples of optional attributes (kwargs): 
           category, creation_date, technologies, keywords.
        ''' 
        self.name = name 
        self.domain = domain 
        self.description = description
        self.author = author
        
        for key in kwargs:
            setattr(self, key, kwargs[key])
 
    def __str__(self): 
        summary = [f'Website "{self.name}"\n',] 
        
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')
            
        return ''.join(summary)


